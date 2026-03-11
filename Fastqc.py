# Step 0: Install required tools if not already
sudo apt-get update
sudo apt-get install -y sra-toolkit wget unzip

# Step 1: Set your SRA accession
SRA_ID="SRR854569"

# Step 2: Download the SRA file
prefetch $SRR854569

# Step 3: Convert SRA to gzipped FASTQ
fasterq-dump $SRR854569.sra --split-files --gzip

# Step 4: Download FastQC if not already
wget -O fastqc.zip "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip"
unzip fastqc.zip
chmod +x FastQC/fastqc

# Step 5: Run FastQC on the downloaded FASTQ files
for fq in ${SRR854569}_*.fastq.gz; do
    ./FastQC/fastqc $fq
done

