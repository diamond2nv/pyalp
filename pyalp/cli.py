if __name__ == '__main__':

    import argparse

    import pyalp.api

    # Command-line parsing.
    parser = argparse.ArgumentParser()
    parser.add_argument("-sn", "--serial-number", type=int,
                        help="serial number of the device to use")
    parser.add_argument("-api", "--api", type=str,
                        help="API to use")
    parser.add_argument("-si", "--skip-interpreter", action="store_true",
                        help="skip the use of the interpreter (development purpose)")
    args = parser.parse_args()

    # Load api.
    api = pyalp.api.load_api(args.api)

    # Handle device.
    dmd = api.handle_device(serial_number=args.serial_number)

    # Allocate device.
    dmd.allocate()

    # Start interpreter (if necessary).
    if args.skip_interpreter:
        pass
    else:
        import IPython
        from traitlets.config import Config

        config = Config()
        config.InteractiveShell.colors = 'Neutral'
        config.InteractiveShell.confirm_exit = False
        config.InteractiveShell.separate_in = ''
        config.InteractiveShell.banner1 = ""
        config.InteractiveShell.banner2 = ""
        IPython.embed(config=config)
        # IPython.embed(display_banner=False)

    # Release device.
    dmd.release()

    # Clean up.
    api.seppuku()
