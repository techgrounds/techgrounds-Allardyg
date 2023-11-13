Week 4 - Azure 1


## Wat is een Azure Region?

https://mycloudit.com/blog/which-azure-region-is-right-for-me

Azure, locally redundant.
What are the paired regions (For Europe, the paired regions are West europe and north europe (ireland)
As you can see, there can be a lot of things to consider when choosing an Azure Region, but typically, our customers tend to choose Azure Regions closer to their physical location, when possible

## Wat is een Azure Availability Zone?

https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview?tabs=azure-cli

Many Azure regions provide availability zones, which are separated groups of datacenters within a region. Availability zones are close enough to have low-latency connections to other availability zones. They're connected by a high-performance network with a round-trip latency of less than 2ms. However, availability zones are far enough apart to reduce the likelihood that more than one will be affected by local outages or weather. Availability zones have independent power, cooling, and networking infrastructure. They're designed so that if one zone experiences an outage, then regional services, capacity, and high availability are supported by the remaining zones. They help your data stay synchronized and accessible when things go wrong.

Not all azure regions support availibility zones, for example when a region doesn't have multiple datacenters. more info https://learn.microsoft.com/en-us/azure/reliability/availability-zones-service-support#azure-regions-with-availability-zone-support

## Wat is een Azure Region Pair?

https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure#azure-paired-regions

https://mycloudit.com/blog/which-azure-region-is-right-for-me

Een azure region pair is de region waar je data naartoe gekopiëerd wordt als je kiest voor geo redundancy

" if you enable geo-redundant storage, Azure will replicate your data to the paired region. For example, if you store your data within the North American East US region, your replicated data will be replicated to the West US Azure Region. "

## Waarom zou je een regio boven een andere verkiezen?

 Selection criteria for choosing the appropriate region generally fall within the following 4 points:

    1. The location closest to the user base
    2. The latency between regions / on-prem
    3. Feature availability in the region
    4. Data residency and compliance

