import datetime
import os
import time
import yaml
import typing
import logging
import pathlib
import argparse
import subprocess

logging.basicConfig(level='DEBUG',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    format="[%(levelname)-s] %(message)-80s")

log = logging.getLogger('build')


def pp_start_job(job: str, module: str):
    log.info("-" * 80)
    log.info("")
    log.info(f"Module: {module}")
    log.info(f"Starting job: {job}")


def pp_finish_job(job: str, module: str, start_time: float, success: bool):
    log.info("-" * 80)
    log.info("Build summary:")
    log.info("")
    log.info(f"Module: {module}")
    log.info(f"Job: {job}")
    log.info("-" * 80)
    if success:
        log.info("BUILD SUCCESS")
    else:
        log.info("BUILD FAILURE")
        log.exception("Error")
    log.info("-" * 80)
    log.info(f"Total time: {time.time() - start_time} s")
    log.info(f"Finished at: {datetime.datetime.now()}")
    log.info("-" * 80)


def evaluate_expression(string: str, execute: bool = True) -> typing.Any:
    """

    :param string:
    :param execute:
    :return:
    """
    if string.strip().lower().startswith('evaluate::sh'):
        command = str(string.split('evaluate::sh')[1:][0]).strip()
        if execute:
            log.info(f"Evaluating sh: {command}")
            process = subprocess.run(command, shell=True, capture_output=True, text=True)
            process.check_returncode()
            return process.stdout.strip()
    if string.strip().lower().startswith('execute::sh'):
        command = str(string.split('execute::sh')[1:][0]).strip()
        if execute:
            log.info(f"Executing sh: {command}")
            result = os.system(command)
            if result != 0:
                raise ValueError(f"{command} unable to execute!")
    if string.strip().lower().startswith('execute::py'):
        command = str(string.split('execute::py')[1:][0]).strip()
        log.info(f"Executing py: {command}")
        exec(command)
    return string


def replace_placeholders(string: str, context: typing.Dict[str, typing.Any]) -> str:
    """

    :param string:
    :param context:
    :return:
    """
    for key in context:
        string = string.replace('${{ ' + key + ' }}', f'{context[key]}')
    return string


def create_context(config: dict) -> dict:
    """

    :param config:
    :return:
    """
    context = {}

    # Project
    self_path = pathlib.Path(__file__).resolve()
    context['project.home'] = os.path.dirname(self_path.resolve())
    context['project.version'] = config['version']
    context['project.profile'] = config['profile']

    # Variables
    if 'vars' in config:
        for var_name in config['vars']:
            context[var_name] = evaluate_expression(replace_placeholders(config['vars'][var_name], context))

    # Modules
    for module_name in config['modules']:
        module = config['modules'][module_name]

        if 'modules' not in context:
            context['modules'] = [module_name]
        else:
            context['modules'].append(module_name)

        module_version = module.get('version', context['project.version'])
        context[f"{module_name}.version"] = replace_placeholders(module_version, context)

        module_path = module['base-path']
        context[f'{module_name}.base-path'] = replace_placeholders(module_path, context)

        if 'vars' in module:
            for var_name in module['vars']:
                context[f'{module_name}.{var_name}'] = replace_placeholders(evaluate_expression(module['vars'][var_name]), context)

        context[f'{module_name}.jobs'] = []
        for job_name in module['jobs']:
            context[f'{module_name}.jobs'].append(job_name)

    return context


def run_job(module: str, job: str, context: dict, application: dict):
    job_config = application['project']['modules'][module]['jobs'][job]
    run_config = job_config['run']

    for execution in run_config:
        evaluate_expression(replace_placeholders(execution, context))


def main(parser: argparse.ArgumentParser) -> typing.NoReturn:
    """

    :param parser:
    :return:
    """
    log.info("")
    log.info("=" * 80)

    args = parser.parse_args()
    application = yaml.unsafe_load(open('application.yml', 'r'))
    context = create_context(application['project'])

    if args.module in context['modules']:
        if args.action == 'run':
            if not args.job:
                parser.error("action 'run' requires --job")

            if args.job not in context[f'{args.module}.jobs']:
                parser.error(f"unknown job '{args.job}', expected any of: {context[f'{args.module}.jobs']}")

            start = time.time()
            pp_start_job(args.job, args.module)
            try:
                run_job(args.module, args.job, context, application)
                pp_finish_job(args.job, args.module, start, True)
            except Exception:
                pp_finish_job(args.job, args.module, start, False)

        elif args.action == 'jobs':
            log.info(f"Jobs for module '{args.module}': {context[f'{args.module}.jobs']}")
        elif args.action == 'version':
            log.info(f"Version for module '{args.module}': {context[f'{args.module}.version']}")

    log.info("=" * 80)
    log.info("")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('module', help='Project module.')
    arg_parser.add_argument('action', help='Action to execute.', choices=['run', 'jobs', 'version'])
    arg_parser.add_argument('--job', dest='job', help='Job defined in application.yml to be executed.')
    arg_parser.add_argument('--version', help="Version", action='version', version='v0.0.1')

    main(arg_parser)
