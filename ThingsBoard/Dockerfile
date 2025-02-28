FROM thingsboard/tb-postgres

# Switch to root user to run apt-get commands
USER root

# Install curl and jq
RUN apt-get update && apt-get install -y curl jq

# Switch back to the 'thingsboard' user after installation
USER thingsboard

# Copy any additional configuration or scripts, if needed
