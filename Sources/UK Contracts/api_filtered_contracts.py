import requests
import json

base_url = "https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json"
keyword = "analysis"

params = {
    "searchCriteria": {
        "types": ["Contract", "Pipeline", "PreProcurement"],
        "statuses": ["Open"],
        "keyword": None,
        "queryString": None,
        "regions": None,
        "postcode": None,
        "radius": 0.0,
        "valueFrom": None,
        "valueTo": None,
        "publishedFrom": None,
        "publishedTo": None,
        "deadlineFrom": None,
        "deadlineTo": None,
        "approachMarketFrom": None,
        "approachMarketTo": None,
        "awardedFrom": None,
        "awardedTo": None,
        "isSubcontract": None,
        "suitableForSme": None,
        "suitableForVco": None,
        "awardedToSme": None,
        "awardedToVcse": None,
        "cpvCodes": [
            "66171000",  # Financial consultancy services
            "73000000",  # Research and development services and related consultancy services
            "73100000",  # Research and experimental development services
            "73110000",  # Research services
            "73120000",  # Experimental development services
            "73200000",  # Research and development consultancy services
            "73210000",  # Research consultancy services
            "73220000",  # Development consultancy services
            "73300000",  # Design and execution of research and development
            "73400000",  # Research and Development services on security and defence materials
            "75210000",  # Foreign affairs and other services
            "75211200",  # Foreign economic-aid-related services
            "79311100",  # Survey design services
            "79311300",  # Survey analysis services
            "79311400",  # Economic research services
            "79311410",  # Economic impact assessment
            "79313000",  # Performance review services
            "79314000",  # Feasibility study
            "79315000",  # Social research services
            "79320000",  # Public-opinion polling services
            "79330000",  # Statistical services
            "79411000",  # General management consultancy services
            "79411100",  # Business development consultancy service
            "79419000",  # Evaluation consultancy services
            "90713000",  # Environmental issues consultancy services
            "98200000",  # Equal opportunities consultancy services
            "80000000"   # Education and training services    
        ]
    },
    "size": 10000
}

# Make the POST request with json data
response = requests.post(base_url, json=params)


if response.status_code == 200:
    # Process and save the data
    data = response.json()
    
    if data:
        output_file = "UK Contracts/output_data.json"  # Save as JSON file
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)  # Save with pretty formatting
        print(f"Data saved to {output_file}")
    else:
        print("No data found.")
else:
    print("Request failed with status code:", response.status_code)
    with open("error_log.txt", "w") as f:
        f.write(response.text)  # Save the raw error response
        print("Error details saved to error_log.txt")
