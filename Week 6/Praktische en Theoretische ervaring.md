# Praktisch:
_________________
## Entra ID

    Waar kan ik Microsoft Entra ID vinden in de console?
    
In het hamburgermenu aan de linkerzijde, bij "Microsoft Entra ID"
![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/6fac8eea-94ea-4bc0-87c5-a79e83f493d8)

    Hoe zet ik Microsoft Entra ID aan?

Microsoft Entra ID staat altijd aan. Zodra je een account maakt heeft dit account automatisch toegang en permissions, en dit kan je door middel van Microsoft Entra ID managen.

    Hoe kan ik Microsoft Entra ID koppelen aan andere resources?

N.V.T.

## Azure Monitor

    Waar kan ik Azure Monitor vinden in de console?
in het hamburgermenu aan de linkerzijde

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/907e51d4-a904-43ec-bc7f-80a45cceaae9)

https://portal.azure.com/#view/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/~/overview


    Hoe zet ik Azure Monitor aan?

De monitor staat altijd aan, maar je moet wel in het overview een selectie maken voordat je inzicht krijgt. Je hebt insights, en Detection, triage, and diagnosis. In de volgende screenshot heb ik onder Detection, triage, and diagnosis de functie Metrics geselecteerd, en mijn CosmosDB geselecteerd.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/6bbb932c-1fca-4722-b723-d848aeb00294)


    Hoe kan ik Azure Monitor koppelen aan andere resources?
    
Bij het maken van een selectie waar je inzicht in wilt hebben krijg je de optie om een resource te selecteren.


## CosmonsDB
  
    Waar kan ik CosmosDB vinden in de console?
  Hamburgermenu linkerzijde, of bij azure monitor onder Insights

  ![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/d64a95d6-54cc-4acc-a63c-d6106cc26b54)


    Hoe zet ik CosmosDB aan?
 Vanuit de CosmosDB pagina kan je een instantie aanmaken, vervolgens kies je een API (NoSQL, PostgreSQL, MongoDB, etc). Hierna maak je een container aan, en krijg je dit scherm te zien:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/8532e08a-be63-4e04-967f-dadf1021222d)

 Vanuit de data explorer is het mogelijk om nieuwe containers aan te maken.
 
    Hoe kan ik CosmosDB koppelen aan andere resources?
    
![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/f5a420a1-be93-40c2-97ab-718e5f6c9745)

in het menu links staat een sectie voor Integrations, vanuit hier maak je je keuze om CosmosDB te koppelen aan andere resources.


## Azure Functions

    Waar kan ik Azure Functions vinden in de console?
    Hoe zet ik Azure Functions aan?
    Hoe kan ik Azure Functions koppelen aan andere resources?


_________________

# praktisch deel 2:
_________________

## Event Grid, Queue Storage, Service Bus

    Waar kan ik deze Event Grid vinden in de console?
    Hoe zet ik Event Grid aan?
    Hoe kan ik Event Grid koppelen aan andere resources?

    Waar kan ik Queue Storage vinden in de console?
    Hoe zet ik Queue Storage aan?
    Hoe kan ik Queue Storage koppelen aan andere resources?

    Waar kan ik Service Bus vinden in de console?
    Hoe zet ik Service Bus aan?
    Hoe kan ik Service Bus koppelen aan andere resources?


__________________

# Theoretisch:
__________________

## Azure Containers

    Welk probleem lost Azure Containers op?
    
Azure Containers voegen alle benodigde bestanden van een functie efficient samen zodat het makkelijker is om te combineren met andere functies.
Microsoft vat het als volgt samen: "A standard package of software—known as a container—bundles an application’s code together with the related configuration files and libraries, and with the dependencies required for the app to run. This allows developers and IT pros to deploy applications seamlessly across environments."

    Welke key termen horen bij Azure Containers?
Agility, Portability, Rapid Scalability, Docker, Kubernetes/K8s

    Hoe past X / vervangt X in een on-premises setting?
Containers zijn zowel mogelijk in ene on-premise setting als een cloud setting

    Hoe kan ik Azure Containers combineren met andere diensten?
Bij het aanmaken van een nieuwe functie is het mogelijk om een container te kiezen, qua design werkt het dus al samen met andere diensten.

    Wat is het verschil tussen Azure Containers en andere gelijksoortige diensten?
AWS heeft ECS (Elastic Container Service), wat een aantal jaar ouder is dan Azure Container apps.

Verder is er deze lijst:
    
    AWS ECS support both Windows and Linux container images. But the public preview of Azure Container currently supports only Linux based container images.
    
    AWS ECS allows you to register and use external physical/VM instances to run the containerized applications. Azure Container apps does not support external instances.
    
    AWS ECS offers Fargate(Serverless), EC2 and external launch types. But Azure Container Apps currently support only serverless container services backed by AKS.
    
    AWS ECS uses Task Definitions to configure the container configurations such as image,
    CPU and memory capacity, launch compatibility, port mappings, health check, environment variables etc.
    
    A revision in Azure Container App defines the container configurations such as image name, CPU and memory, environment variables and scale settings.
    
    A task in ECS runs the containers inside the ECS cluster. A Pod in Azure container app is used to run one or more containers inside the Container App.
    
    Azure Container App support Dapr and Envoy for building and deploying microservices. ECS uses AWS App Mesh backed by Envoy to deploy microservices.
    
    ECS support Application Load Balancer, Network Load Balancer or Classic Load Balancer for applications that require Http inbound support.
    Azure Container App uses Http Ingress to support Http inbound traffic from outside the cluster.
    
    ECS clusters runs inside the default VPC or a user defined VPC. Azure Container App can be deployed in a default VNET or a custom VNET defined by user.
    
    An ECS service allows you to deploy containers either using rolling update strategy or BlueGreen deployment strategy.
    Multiple Revision mode and traffic splitting policy in Azure Container App allows you to enable A/B testing and BlueGreen deployment of applications.

https://synergetics1.wordpress.com/2022/05/11/azure-container-apps-compared-with-aws-elastic-container-service/


## Azure Support Plans


    Welk probleem lost Azure Support Plans op?
    Welke key termen horen bij Azure Support Plans?
    Hoe past X / vervangt X in een on-premises setting?
    Hoe kan ik Azure Support Plans combineren met andere diensten?
    Wat is het verschil tussen Azure Support Plans en andere gelijksoortige diensten?


## Azure Advisor


    Welk probleem lost Azure Advisor op?
    Welke key termen horen bij Azure Advisor?
    Hoe past X / vervangt X in een on-premises setting?
    Hoe kan ik Azure Advisor combineren met andere diensten?
    Wat is het verschil tussen Azure Advisor en andere gelijksoortige diensten?

## Azure App Configuration


    Welk probleem lost Azure App Configuration op?
    Welke key termen horen bij Azure App Configuration?
    Hoe past X / vervangt X in een on-premises setting?
    Hoe kan ik Azure App Configuration combineren met andere diensten?
    Wat is het verschil tussen Azure App Configuration en andere gelijksoortige diensten?


## Azure Monitor Logs


    Welk probleem lost Azure Monitor Logs op?
    Welke key termen horen bij Azure Monitor Logs?
    Hoe past X / vervangt X in een on-premises setting?
    Hoe kan ik Azure Monitor Logs combineren met andere diensten?
    Wat is het verschil tussen Azure Monitor Logs en andere gelijksoortige diensten?

