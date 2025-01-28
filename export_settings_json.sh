#!/bin/bash  
  
# Read the existing settings.json file  
existing_settings=$(cat settings.json)  
  
# Process the .env file  
while IFS='=' read -r key value; do  
  # Remove double quotes from the line  
  value=${value//\"/}  
    
  # Check if the line is commented out  
  if [[ $key =~ ^# ]]; then  
    continue  
  fi  
  
  # Check if the key-value pair is valid  
  if [[ ! -z "$key" && ! -z "$value" ]]; then  
    # Create a new JSON object  
    new_setting=$(jq -n --arg name "$key" --arg value "$value" '{name: $name, slotSetting: false, value: $value}')  
  
    # Add the new JSON object to the existing settings  
    existing_settings=$(jq -n  --argjson new_setting "$new_setting"  --argjson existing_settings "$existing_settings"  '$existing_settings + [$new_setting]')  
  fi  
done < .env  
  
# Write the updated settings to the settings.json file  
echo "$existing_settings" > settings.json  

