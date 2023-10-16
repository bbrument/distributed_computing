# Source the conda environment and change directory
source /home/lilian/anaconda3/etc/profile.d/conda.sh
conda activate neus
cd /media/disk1/Baptiste/Playing_with_NeuS

# Check if a command was provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <command>"
  exit 1
fi

# Execute the provided command
command="$1"
eval "$command" #>&2