# Enable MIG on GPU devices
nvidia-smi -i 0 -mig 1
nvidia-smi -i 1 -mig 1
nvidia-smi -i 2 -mig 1
nvidia-smi -i 3 -mig 1
# Might be able to enable with this, otherwise reboot
nvidia-smi --gpu-reset

nvidia-smi mig -cgi "5,19,19,19" -C
# List all devices/MIGs with device IDs
nvidia-smi -L
# Create MIG on GPU 0 with profiles 19
sudo nvidia-smi mig -i 0 -cgi "19,19,19,19,19,19,19" -C
# Delete all MIGs
sudo nvidia-smi mig -dci && sudo nvidia-smi mig -dgi
