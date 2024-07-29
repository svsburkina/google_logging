# Adding Google Cloud Logging to Odoo

This guide provides step-by-step instructions to manually add Google Cloud Logging to your Odoo instance.

## Prerequisites

- Odoo installed and running.
- A Google Cloud account with a service account key.
- The `google-cloud-logging` Python package.

## Step-by-Step Guide

### 1. Install the Google Cloud Logging Python Package

First, install the `google-cloud-logging` package using pip:

```bash
pip install google-cloud-logging
```

### 2.Ensure the Service Account Credentials
```bash
sudo mkdir -p /etc/google-cloud
sudo mv /path/to/YOUR_KEY_FILE.json /etc/google-cloud/
sudo chmod 600 /etc/google-cloud/YOUR_KEY_FILE.json
```

### 3. Set the GOOGLE_APPLICATION_CREDENTIALS Environment Variable
Add the environment variable to the system-wide profile:

```bash
sudo nano /etc/profile
```
Add the following line to the end of the file:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/etc/google-cloud/YOUR_KEY_FILE.json"
```
Save and close the file, then apply the changes:

```bash
source /etc/profile
``` 


### 4. Modify Odoo Configuration
Create a custom module for logging in Odoo. Open or create the following file:
    
```bash
sudo nano /path/to/your/odoo/custom_addons/google_logging/__init__.py
```

### 5. Ensure the Custom Module is Loaded
Make sure the custom module is loaded when Odoo starts. Edit your Odoo configuration file (usually odoo.conf or odoo-server.conf) and add the custom module to the list of installed addons:
```ini
[options]
addons_path = /path/to/your/odoo/custom_addons,/path/to/other/addons
```
Ensure your custom module (google_logging) is included in the addons_path.

### 6. Restart Odoo
Restart your Odoo server to apply the changes:

```bash
sudo systemctl restart odoo
```

### 7. Verify the Logs
Check the Google Cloud Logging dashboard to verify that logs are being sent:

Go to the [Google Cloud Logging](https://console.cloud.google.com/logs/viewer)  dashboard to verify that logs are being sent from Odoo.


