# Hello World NodeServer (PG3x)

A minimal "Hello World" Polyglot v3 NodeServer for Universal Devices ISY systems. This serves as a basic template and learning example for developers who want to create their own NodeServers.

## What is this?

This is a minimal example NodeServer for the [Universal Devices ISY](https://www.universal-devices.com/) home automation system using the Polyglot v3 framework. It demonstrates the basic structure and required components for a functional NodeServer without any complex functionality.

## Prerequisites

- Universal Devices ISY controller
- Polyglot v3 system (IoP or standalone)
- Python 3.6+ (handled by Polyglot)
- **Developer Account**: You must become a registered developer with Universal Devices by opening a support ticket and requesting developer access

## Features

- Single controller node with basic status reporting
- Minimal code demonstrating Polyglot v3 event handling
- Ready-to-use ISY profile with node definitions
- Clean implementation suitable as a starting template

## Installation

**Important**: Before installing any NodeServer, you must first become a registered developer with Universal Devices. Open a support ticket at [Universal Devices Support](https://www.universal-devices.com/support/) and request developer access.

**Note**: This NodeServer can only be installed via the **LOCAL store** on your Polyglot v3 system. You must first create a LOCAL store item in your Polyglot system before you can install it.

### Steps to Install:

1. **Become a Developer**: Request developer access from Universal Devices (see above)
2. **Get the Code**: Download or clone this repository to your local machine
3. **Choose Installation Method**:

   **Method A: ZIP File Upload**
   - Create a ZIP file of the entire project directory
   - Log into your Polyglot v3 system web interface
   - Go to the NodeServer Store
   - Create a new LOCAL store item
   - Upload your ZIP file

   **Method B: Direct Copy to Device (Development Mode)**
   - Copy the entire `ISYHelloWorld` directory to your ISY device (eisy or Polisy)
   - Default location: `/home/admin/plugins/ISYHelloWorld/`
   - Log into your Polyglot v3 system web interface
   - Go to the NodeServer Store
   - Create a new LOCAL store item in development mode
   - Point the store to the directory location: `/home/admin/plugins/ISYHelloWorld/`

4. **Install**: Install the NodeServer from your LOCAL store
5. **Start**: Start the NodeServer through Polyglot
6. **Verify**: The Hello World Controller node will appear in your ISY

### For Development:
```bash
git clone https://github.com/awysocki/ISYHelloWorld.git

# Method A: Create ZIP for upload
# Method B: Copy to device
scp -r ISYHelloWorld admin@your-device-ip:/home/admin/plugins/
```

**Note**: Replace `your-device-ip` with your ISY device's IP address.

## Usage

The NodeServer creates a single "Hello World Controller" node that:
- Reports online status (ST = 1)
- Responds to Query commands (though they don't perform any real actions)
- Updates status periodically via long poll
- Demonstrates basic NodeServer lifecycle events

**Note:** This is purely an example - it doesn't control any real devices or provide useful functionality beyond demonstrating the NodeServer structure.

## Development

If you want to use this as a starting point for your own NodeServer:

1. Fork this repository
2. Modify `server.py` to add your custom functionality
3. Update `server.json` with your NodeServer details
4. Modify the profile files in `profile/` to match your nodes and capabilities
5. Test with your Polyglot system

## Files Structure

- `server.py` - Main NodeServer implementation
- `server.json` - NodeServer metadata (name, version, etc.)
- `requirements.txt` - Python dependencies (`udi-interface`)
- `install.sh` - Installation script for Polyglot
- `profile/` - ISY profile definitions
  - `nodedef/node.def` - Node type definitions
  - `editor/editors.xml` - Editor definitions for ISY
  - `nls/en_us.txt` - Text strings for ISY interface

## Contributing

This is a simple example project, but if you find bugs or have suggestions for making it a better learning template, feel free to open an issue or submit a pull request.

## Resources

- [Universal Devices ISY](https://www.universal-devices.com/)
- [Polyglot v3 Documentation](https://polyglot.universal-devices.com/)
- [UDI Interface Library](https://github.com/UniversalDevicesInc/udi-interface)

## Troubleshooting

**NodeServer doesn't appear in ISY**
- Ensure you have developer access from Universal Devices
- Check that the NodeServer is started in Polyglot
- Verify your ISY is properly connected to Polyglot

**Installation fails**
- Ensure all files are included in your ZIP or directory copy
- Check that the `requirements.txt` file is present
- Verify Python dependencies are installing correctly
- Check the **System Logs** in the Polyglot v3 web interface for loading errors

**"Hello World Controller" node shows offline**
- Check Polyglot logs for any Python errors
- Ensure the ISY profile version matches the NodeServer version (1.0.8)
- Try restarting the NodeServer in Polyglot

**General Debugging**
- Use the **LOG files** on the Polyglot v3 web page to view messages:
  - **System Logs**: Check here if the NodeServer fails to load initially
  - **NodeServer Logs**: Once loaded, check the "ISYHelloWorld" NodeServer logs for runtime issues
- Log files are accessible through the Polyglot web interface under the Logs section

## License

This project is released into the public domain under the Unlicense - see the [LICENSE](LICENSE) file for details.

## Version

1.0.8 - Minimal production release