# Use the Selenium standalone Chrome image
FROM selenium/standalone-chrome:latest

# Set the working directory in the container
WORKDIR /app

# Switch to root user to install packages
USER root

# Install Python and Xvfb
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    xvfb 

# Copy the Python script, requirements file, and entrypoint script
COPY services.py apps.py requirements.txt entrypoint.sh ./

# Activate virtual environment and install Python dependencies
RUN python3 -m pip install --break-system-packages -r requirements.txt

# Set permissions for entrypoint script
RUN chmod +x /app/entrypoint.sh

# Ensure the data directory exists
RUN mkdir -p /app/data

# Copy the Excel file into the container
COPY 5000_list.xlsx google-services.json GoogleService-Info.plist service_account.json /app/data/

# Expose the Flask application port
EXPOSE 8080

# Set non-root user for running the application if possible
# USER selenium-user

# Set entrypoint and CMD
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python3", "apps.py"]





# FROM python:3.6

# # Set the working directory in the container
# WORKDIR /app

# # Copy the Python script and requirements file to the container
# COPY Supertel.py requirements.txt ./

# # Install required libraries
# RUN apt-get update \
#  && apt-get install -y libnss3 libnspr4

# # Install Google Chrome
# RUN wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.89/linux64/chrome-linux64.zip \
#  && unzip chrome-linux64.zip -d /opt/chrome \
#  && ln -s /opt/chrome/chrome-linux64/chrome /usr/bin/google-chrome \
#  && rm chrome-linux64.zip

# # Install Chromedriver
# RUN wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.89/linux64/chromedriver-linux64.zip \
#  && unzip chromedriver-linux64.zip -d /usr/local/bin/ \
#  && chmod +x /usr/local/bin/chromedriver-linux64/chromedriver \
#  && rm chromedriver-linux64.zip

# # Install xvfb
# RUN apt-get update \
#  && apt-get install -yqq xvfb

# # Set display port and dbus env to avoid hanging
# ENV DISPLAY=:99
# ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# # Upgrade pip and install Python dependencies
# RUN pip install --upgrade pip \
#  && pip install --no-cache-dir -vvv -r requirements.txt

# # Expose the Flask application port
# EXPOSE 8080

# # Run the Python script
# CMD ["python", "Supertel.py"]
