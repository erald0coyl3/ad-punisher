from os.path import isfile
from colorama import init, Fore
from configs.config import CONFIG
from traceback import format_exc as print_traceback
from argparse import ArgumentParser, SUPPRESS, HelpFormatter
from bot_lib.bot_functions import ads_click_flooding, get_free_proxies, find_targets


class CustomHelpFormatter(HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=50, width=100)

    def format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super().format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string


def main(arguments: ArgumentParser) -> None:
    """
    manages all procedures of the program
    :param arguments: command line argparse object
    :return: None
    """
    parser = arguments.parse_args()
    if not parser.file and not isfile(parser.file):
        arguments.print_help()
        return

    print(CONFIG["logs"]["process_start"].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
    print(CONFIG["logs"]["process_get_urls"].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
    collected_urls = find_targets(parser.file)

    if not collected_urls:
        print(CONFIG["logs"]["process_ads_empty"].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        return

    print(CONFIG["logs"]["process_kill_prep"].format(Fore.LIGHTRED_EX,
                                                     Fore.LIGHTWHITE_EX,
                                                     Fore.LIGHTRED_EX,
                                                     Fore.LIGHTWHITE_EX))
    ads_click_flooding(collected_urls, get_free_proxies())

    print(CONFIG["logs"]["process_done"].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))


if __name__ == "__main__":
    arg_style = lambda prog: CustomHelpFormatter(prog)
    args = ArgumentParser(description=CONFIG["argparse"]["description"],
                          add_help=False,
                          formatter_class=arg_style)
    group_required = args.add_argument_group(title="required arguments")
    group_required.add_argument("-f", "--file", metavar="file", type=str, help=CONFIG["argparse"]["file"])
    group_optional = args.add_argument_group(title="optional arguments")
    group_optional.add_argument("-h", "--help", help=CONFIG["argparse"]["help"], action="help", default=SUPPRESS)

    try:
        # perform coloroma multiplatform
        init(strip=False)

        print(CONFIG['logs']['presentation']['logo'].format(Fore.LIGHTWHITE_EX),
              CONFIG['logs']['presentation']['description'].format(Fore.LIGHTRED_EX,
                                                                   Fore.LIGHTWHITE_EX,
                                                                   Fore.LIGHTRED_EX,
                                                                   Fore.LIGHTWHITE_EX))
        main(arguments=args)

    except KeyboardInterrupt:
        print(CONFIG['logs']['key_interrupt'].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, print_traceback()))
    except Exception:
        print(CONFIG['logs']['error_start_bot'].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, print_traceback()))

