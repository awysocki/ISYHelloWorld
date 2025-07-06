#!/usr/bin/env python3
"""
Hello World NodeServer for Polyglot v3
A minimal example demonstrating basic NodeServer functionality.

This is free and unencumbered software released into the public domain.
For more information, please refer to <https://unlicense.org>
"""
import udi_interface
import sys

__version__ = "1.0.8"

LOGGER = udi_interface.LOGGER

class HelloWorldController(udi_interface.Node):
    """Main controller node for Hello World NodeServer"""
    
    def __init__(self, polyglot, primary, address, name):
        super().__init__(polyglot, primary, address, name)
        self.name = name

    def start(self):
        """Called when the node starts"""
        LOGGER.info("Hello World Controller started")
        self.setDriver('ST', 1)

    def stop(self):
        """Called when the node stops"""
        LOGGER.info("Hello World Controller stopped")

    def query(self, command=None):
        """Called when ISY queries the node"""
        self.reportDrivers()

    def shortPoll(self):
        """Called every shortPoll seconds"""
        pass

    def longPoll(self):
        """Called every longPoll seconds"""
        self.setDriver('ST', 1)

    # Define the drivers (status values) for this node
    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2}
    ]

    # Define the node ID (must match nodedef)
    id = 'HELLO'

    # Define the commands this node supports
    commands = {
        'QUERY': query
    }

if __name__ == "__main__":
    try:
        LOGGER.info(f"Starting Hello World NodeServer v{__version__}")
        
        # Create the polyglot interface
        polyglot = udi_interface.Interface([])
        controller = None
        
        # Event handlers
        def handle_start():
            global controller
            if controller is None:
                controller = HelloWorldController(polyglot, 'controller', 'controller', 'Hello World Controller')
                polyglot.addNode(controller)
                controller.start()
        
        def handle_stop():
            if controller:
                controller.stop()
        
        def handle_poll(pollflag):
            if controller:
                if 'shortPoll' in pollflag:
                    controller.shortPoll()
                elif 'longPoll' in pollflag:
                    controller.longPoll()
        
        def handle_config(config):
            global controller
            if controller is None:
                controller = HelloWorldController(polyglot, 'controller', 'controller', 'Hello World Controller')
                polyglot.addNode(controller)
                controller.start()
                controller.reportDrivers()
            else:
                controller.reportDrivers()
        
        # Subscribe to events
        polyglot.subscribe(polyglot.START, handle_start)
        polyglot.subscribe(polyglot.STOP, handle_stop)
        polyglot.subscribe(polyglot.POLL, handle_poll)
        polyglot.subscribe(polyglot.CONFIG, handle_config)
        
        # Start the interface
        polyglot.start()
        polyglot.ready()
        LOGGER.info("Hello World NodeServer ready and running")
        polyglot.runForever()
        
    except KeyboardInterrupt:
        LOGGER.info("Hello World NodeServer shutting down...")
        if controller:
            controller.stop()
        sys.exit(0)
    except Exception as e:
        LOGGER.error(f"Fatal error in NodeServer: {e}")
        sys.exit(1)
