import os
#
# def unblock_website(website):
#     hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
#     with open(hosts_path, "r") as file:
#         lines = file.readlines()
#     with open(hosts_path, "w") as file:
#         for line in lines:
#             if website not in line:
#                 file.write(line)
#
# # Example usage:
# website_to_unblock = "example.com"
# unblock_website(website_to_unblock)

def block_websites(websites):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Path to the hosts file on Windows

    # Add entries to block websites in the hosts file
    with open(hosts_path, "a") as hosts_file:
        for website in websites:
            hosts_file.write("127.0.0.1 " + website + "\n")

    print("Websites blocked successfully.")

# List of websites to block
websites_to_block = ["example.com"]

# Call the function to block the websites
block_websites(websites_to_block)