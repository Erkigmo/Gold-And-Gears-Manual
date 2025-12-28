def get_all_domain_names() -> list:
	domain_names = []

	domain_names.append("Combat")
	domain_names.append("Elite")
	domain_names.append("Occurrence")
	domain_names.append("Occurrence Abnormal")
	domain_names.append("Reward")
	domain_names.append("Adventure")
	domain_names.append("Intra-Cognition")
	domain_names.append("Transaction")
	domain_names.append("Blank")
	domain_names.append("Respite")
	domain_names.append("Boss")

	return domain_names

# Returns the optional domains to complete a run
def get_optional_domain_names() -> list:
	domain_names = []

	domain_names.append("Elite")
	domain_names.append("Occurrence")
	domain_names.append("Occurrence Abnormal")
	domain_names.append("Reward")
	domain_names.append("Adventure")
	domain_names.append("Intra-Cognition")
	domain_names.append("Blank")

	return domain_names

def get_secrets() -> list:
	trailblaze_secrets = []

	trailblaze_secrets.append({"Beginning: Interastral Peace Corporation", 1})
	trailblaze_secrets.append({"Judged as Organic: Associates (I)", 1})
	trailblaze_secrets.append({"Broadened Cognition: Associates (II)", 1})
	trailblaze_secrets.append({"Judged as Inorganic: Liquid Gold (I)", 1})
	trailblaze_secrets.append({"Broadened Cognition: Liquid Gold (II)", 1})

	trailblaze_secrets.append({"Beginning: The Machine Empire", 1})
	trailblaze_secrets.append({"Judged as Organic: Bad Thought (I)", 1})
	trailblaze_secrets.append({"Broadened Cognition: Bad Thought (II)", 1})
	trailblaze_secrets.append({"Judged as Inorganic: The Suffering *Father* (I)", 1})
	trailblaze_secrets.append({"Broadened Cognition: The Suffering *Father* (II)", 1})

	trailblaze_secrets.append({"Supreme Organic: Sanguine Condolences (I)", 3})
	trailblaze_secrets.append({"Supreme Organic: Sanguine Condolences (II)", 3})
	trailblaze_secrets.append({"Supreme Inorganic: Sanguine Condolences (III)", 3})
	trailblaze_secrets.append({"Supreme Inorganic: Universe's Throne (I)", 3})
	trailblaze_secrets.append({"Broadened Cognition: Universe's Throne (II)", 3})
	trailblaze_secrets.append({"Supreme Organic: Mental Spices (I)", 3})
	trailblaze_secrets.append({"Supreme Organic: Mental Spices (II)", 3})
	trailblaze_secrets.append({"Supreme Inorganic: God's Three Revalations (I)", 3})
	trailblaze_secrets.append({"Supreme Organic: God's Three Revalations (II)", 3})
	trailblaze_secrets.append({"Supreme Organic: God's Three Revalations (III)", 3})

	return trailblaze_secrets

def generate_domain_checks(name: str, amount: int) -> list:
	location_table = []

	for a in range(amount):
		location_table.append({
			'name': "Complete " + name + " Domain" + " - " + str(a + 1),
			'category': ["Domains"],
			'requires': "|" + name + " Domain|"
		})
	return location_table

def generate_excess_domain_names(name: str, start: int, end: int) -> list:
	location_table = []

	difference = end - start

	for a in range(difference + 1):
		location_table.append(
			"Complete " + name + " Domain" + " - " + str(a + start)
		)

	return location_table