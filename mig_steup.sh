nvidia-smi -i 0 -mig 1
nvidia-smi -i 1 -mig 1
nvidia-smi -i 2 -mig 1
nvidia-smi -i 3 -mig 1
nvidia-smi --gpu-reset

nvidia-smi mig -cgi "5,19,19,19" -C
nvidia-smi -L
# sudo nvidia-smi mig -i 0 -cgi "19,19,19,19,19,19,19" -C
# nvidia-smi mig -dci && sudo nvidia-smi mig -dgi
