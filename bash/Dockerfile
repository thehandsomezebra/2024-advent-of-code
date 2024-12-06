# FROM ubuntu:latest

# # Install the latest version of bash
# RUN apt-get update && \
#     apt-get install -y bash

# # Copy the script and input file into the container
# COPY 4.sh /4.sh
# COPY 4-input.txt /4-input.txt

# # Make the script executable
# RUN chmod +x /4.sh

# # Run the script and capture the output
# CMD bash /4.sh /4-input.txt

FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y bash

COPY . /app

WORKDIR /app/bash

CMD ["bash", "-c", "echo 'Have fun with Bash during Advent of Code 2024'"]
