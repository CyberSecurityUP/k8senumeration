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
    print("20. Lists AWS EKS clusters (with optional region)")
    print("21. Describes an AWS EKS cluster (with optional cluster name and region)")
    print("22. Lists AWS EKS node groups (with cluster name and optional region)")
    print("0. Exit")

    choice = input("Option: ")

    if choice == "0":
        break
    elif choice in ["1", "2", "3", "5", "6", "7", "9", "13"]:
        command = f"kubectl "
        if choice == "1":
            command += "config get-users"
            output_file = "container_getusers.txt"
            execute_command(command, output_file)
        elif choice == "2":
            command += "config get-contexts"
            output_file = "container_getcontexts.txt"
            execute_command(command, output_file)
        elif choice == "3":
            command += "config get-clusters"
            output_file = "container_getclusters.txt"
            execute_command(command, output_file)
        elif choice == "5":
            command += "get roles"
            output_file = "container_getroles.txt"
            execute_command(command, output_file)
        elif choice == "6":
            command += "get clusterroles"
            output_file = "container_clusterroles.txt"
            execute_command(command, output_file)
        elif choice == "7":
            command += "get namespaces"
            output_file = "container_getnamespace.txt"
            execute_command(command, output_file)
        elif choice == "9":
            command += "get serviceaccounts"
            output_file = "container_getserviceaccounts.txt"
            execute_command(command, output_file)
        elif choice == "13":
            command += "get nodes"
            output_file = "container_getnodes.txt"
            execute_command(command, output_file)
    elif choice in ["4", "8", "10", "11", "12", "16"]:
        command = "kubectl "
        if choice == "4":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"auth can-i --list -n {namespace}"
            else:
                command += "auth can-i --list"
            output_file = "container_authcans.txt"
            execute_command(command, output_file)
        elif choice == "8":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get secrets -o yaml -n {namespace}"
            else:
                command += "get secrets -o yaml"
            output_file = "container_getsecrets.txt"
            execute_command(command, output_file)
        elif choice == "10":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get deployments -n {namespace}"
            else:
                command += "get deployments"
            output_file = "container_getdeployments.txt"
            execute_command(command, output_file)
        elif choice == "11":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get pods -n {namespace}"
            else:
                command += "get pods"
            output_file = "container_getpods.txt"
            execute_command(command, output_file)
        elif choice == "12":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get services -n {namespace}"
            else:
                command += "get services"
            output_file = "container_getservices.txt"
            execute_command(command, output_file)
        elif choice == "16":
            namespace = input("Enter the namespace (optional, press Enter to skip): ")
            if namespace:
                command += f"get configmaps -n {namespace}"
            else:
                command += "get configmaps"
            output_file = "container_getconfigmaps.txt"
            execute_command(command, output_file)
    elif choice in ["14", "15"]:
        command = "kubectl "
        if choice == "14":
            command += "get daemonsets"
            output_file = "container_daemonsets.txt"
            execute_command(command, output_file)
        elif choice == "15":
            command += "get cronjobs"
            output_file = "container_getcronjob.txt"
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
    elif choice in ["20", "21", "22"]:
        if choice == "20":
            region = input("Enter the region (optional, press Enter to skip): ")
            command = "aws eks list-clusters"
            if region:
                command += f" --region {region}"
            output_file = "aws_eks_list_clusters.txt"
            execute_command(command, output_file)
        elif choice == "21":
            cluster_name = input("Enter the cluster name (optional, press Enter to skip): ")
            region = input("Enter the region (optional, press Enter to skip): ")
            command = "aws eks describe-cluster"
            if cluster_name:
                command += f" --name {cluster_name}"
            if region:
                command += f" --region {region}"
            output_file = "aws_eks_describe_cluster.txt"
            execute_command(command, output_file)
        elif choice == "22":
            cluster_name = input("Enter the cluster name: ")
            region = input("Enter the region (optional, press Enter to skip): ")
            command = "aws eks list-nodegroups"
            if cluster_name:
                command += f" --cluster {cluster_name}"
            if region:
                command += f" --region {region}"
            output_file = "aws_eks_list_nodegroups.txt"
            execute_command(command, output_file)
    else:
        print("Invalid option. Try again.")

print("Script Finished.")
