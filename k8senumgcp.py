import subprocess

def execute_command(command, output_file):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        with open(output_file, 'w') as file:
            file.write(result.stdout)
        print(f"Command '{command}' executed successfully. Result saved in {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing '{command}': {e.stderr}")

while True:
    print("CREATED BY JOAS A SANTOS v0.1")
    print("Choose an option:")
    print("1. Lists the configured users kubectl")
    print("2. Lists the available contexts configured")
    print("3. Lists the available clusters configured")
    print("4. Lists the permission the current user has in the cluster")
    print("5. Lists the roles available in the cluster")
    print("6. Lists the cluster roles available in the Cluster")
    print("7. Lists the namespace in the cluster")
    print("8. Lists the secrets in the cluster and displays details in YAML format")
    print("9. Lists the service accounts in the cluster")
    print("10. Lists the deployments in the cluster")
    print("11. Lists the running pods in the cluster")
    print("12. Lists the available services in the cluster")
    print("13. Lists the available nodes in the cluster.")
    print("14. Lists the daemon sets in the cluster.")
    print("15. Lists the cron jobs in the cluster.")
    print("16. Lists the config maps in the cluster (with optional namespace)")
    print("17. Lists container images in Google Cloud (with optional repository)")
    print("18. Describes a container image in Google Cloud (with optional name)")
    print("19. Lists Google Cloud container clusters (with optional cluster name and region)")
    print("0. Exit")

    choice = input("Option: ")

    if choice == "0":
        break
    elif choice in ["1", "2", "3", "5", "6", "7", "9", "13"]:
        command = f"kubectl "
        output_file = f"{choice}.txt"
        if choice == "1":
            command += "config get-users"
        elif choice == "2":
            command += "config get-contexts"
        elif choice == "3":
            command += "config get-clusters"
        elif choice == "5":
            command += "get roles"
        elif choice == "6":
            command += "get clusterroles"
        elif choice == "7":
            command += "get namespaces"
        elif choice == "9":
            command += "get serviceaccounts"
        elif choice == "13":
            command += "get nodes"

        execute_command(command, output_file)
    elif choice in ["4", "8", "10", "11", "12", "16"]:
        command = "kubectl "
        output_file = f"{choice}.txt"
        if choice == "4":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"auth can-i --list -n {namespace}"
            else:
                command += "auth can-i --list"
        elif choice == "8":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get secrets -o yaml -n {namespace}"
            else:
                command += "get secrets -o yaml"
        elif choice == "10":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get deployments -n {namespace}"
            else:
                command += "get deployments"
        elif choice == "11":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get pods -n {namespace}"
            else:
                command += "get pods"
        elif choice == "12":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get services -n {namespace}"
            else:
                command += "get services"
        elif choice == "16":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get configmaps -n {namespace}"
            else:
                command += "get configmaps"

        execute_command(command, output_file)
    elif choice == "17":
        repository = input("Enter the repository (optional, press Enter to skip): ")
        command = f"gcloud container images list"
        if repository:
            command += f" --repository={repository}"
        output_file = "container_images.txt"
        execute_command(command, output_file)
    elif choice == "18":
        name = input("Enter the image name (optional, press Enter to skip): ")
        command = "gcloud container images describes"
        if name:
            command += f"{name}"
        output_file = "container_image_describe.txt"
        execute_command(command, output_file)
    elif choice == "19":
        cluster_name = input("Enter the cluster name (optional, press Enter to skip): ")
        region = input("Enter the region (optional, press Enter to skip): ")
        command = "gcloud container clusters describe"
        if cluster_name:
            command += f" {cluster_name}"
        if region:
            command += f" --region={region}"
        output_file = "container_clusters.txt"
        execute_command(command, output_file)
    else:
        print("Invalid option. Try again.")

print("Script Finished.")

