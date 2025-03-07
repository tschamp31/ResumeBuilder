from docxtpl import DocxTemplate

resume = DocxTemplate("Templates/BaseTemplate.docx")
job_array = []
qual_array = []
x = 0
y = 0

prof_job_exp_context = [
	{
		"prof_exp_company":"Wise Agent",
		"prof_exp_job_title_1":"Software Engineer",
		"prof_exp_job_title_2":"Database Architect",
		"prof_exp_date_range":"2022-Present",
		"prof_exp_roles":[
			"Develop solutions for tickets and feature requests.",
			"Provide technical support to call center staff on topic relating to the CRM software and other more personal levels of technical support.",
			"Upgrade existing ASP.Net to a more modern .Net 4.8 and above.",
			"Converting ASP pages to more modern Angular design and flow."
		]
	},
	{
		"prof_exp_company":"Hammoq",
		"prof_exp_job_title_1":"MLOps Engineer",
		"prof_exp_job_title_2":"Principal Full Stack Engineer",
		"prof_exp_date_range":"2020-2022",
		"prof_exp_roles":[
			"Originally hired to work with an outsourced development team which was putting together a proof-of-concept service/website.",
			"Updated proof-of-concept to a production level service.",
			"Oversaw DevOps/MLOPs Implementation/Design/Innovation.",
			"Managed Google Cloud/GitHub/Azure/Slack/Etc.",
			"Managed hardware acquisition, building, and installation to datacenter rental rack for ML training.",
			"Likely additional efforts not listed, feel free to inquire."
		]
	},
	{
		"prof_exp_company":"MedImpact",
		"prof_exp_job_title_1":"Full Stack Developer",
		"prof_exp_job_title_2":"Prior Authorization Coordinator",
		"prof_exp_date_range":"2018-2020",
		"prof_exp_roles":[
			"Obtained subject matter expertise on the processes within the prior authorization pillar of the company.",
			"Applied newly acquired subject matter expertise to advice on improvements in processes and or software."
			"Contributed to the SDLC of the software I had provided input on.",
		]
	},
]

qualifications = [
	{
		"qualification_header": "Personal",
		"qualification_list": [
			"Autodidact – Interested in learning just for the achievement of bettering one’s knowledge and intelligence.",
			"Polymath – Interested in cross disciplinary topics nearing minimally of a bachelor level understanding."
		]
	},
	{
		"qualification_header": "Pharmacy",
		"qualification_list": [
			"PTCB Certified"
			"Arizona State Board of Pharmacy Technician"
		]
	},
	{
		"qualification_header": "Technology",
		"qualification_list": [
			"COMPTIA Training in, A+, Cloud Essentials, Cloud+, and Network+",
			"Kubernetes, Docker, GKE",
			"Springboot, Flask, Django, NodeJS/Express",
			"Tensorflow, PyTorch",
			"Angular, React",
			"SOAP, REST, gRPC, GraphQL, FastAPI",
			"Ability to read documentation and absorb new APIs with ease.",
			"Capable of quickly picking up packages or SDKs for languages.",
			"Microservice/Monolithic Architecture",
			"Agile/Waterfall SDLC",
			"Kanban, Jira, GitHub, Bitbucket, Azure etc.",
			"C++, Java, Python, JavaScript, C#, C, .NET, ASP, VBAScript",
			"(My)SQL, MongoDB, AirTable, Firebase",
			"Android, Linux (Multiple Distro Flavors), iOS, Windows Desktop, Windows Server",
			"Other, willing to learn or likely worked with in past but not listed",
		]
	}
]

objective = {
	"titles": ["Process Optimization","Communications Liaison","Creative Solutions"],
	"examples": ["Driven to improve processes within a professional environment to make them more effective and efficient.", "Ability to provide solutions for relationships between customer, business, and technical teams.", "Evaluate whether there is a solution for the need already or develop one based on time constraints with a debt analysis included."],
}


for prof_exp in prof_job_exp_context:
	job_docx = DocxTemplate("Templates/ProfExpTemplate.docx")
	job_docx.render(prof_exp)
	job_sub_doc = resume.new_subdoc()
	job_sub_doc.subdocx = job_docx
	job_array.append(job_sub_doc)

for qual in qualifications:
	qual_docx = DocxTemplate("Templates/QualTemplate.docx")
	qual_docx.render(qual)
	qual_sub_doc = resume.new_subdoc()
	qual_sub_doc.subdocx = qual_docx
	qual_array.append(qual_sub_doc)


objective_docx = DocxTemplate("Templates/ObjectiveTemplate.docx")
objective_docx.render(objective)
objective_sub_doc = resume.new_subdoc()
objective_sub_doc.subdocx = objective_docx

context = {
	"my_name":"Tyler Champagne",
	"current_address":"17031 E Calle Del Oro Fountain Hills, AZ",
	"contact_email":"tyler@tylerchampagne.dev",
	"contact_number":"Cell: 480-818-5193",
	"github_url":"https://github.com/tschamp31/",
	"objective_description":"Software engineer who creates more effective automation and communication within a company and between the customer and business. Results include saving money and reducing process man hours while improving the customer experience.",
	"core_objectives": objective_sub_doc,
	"accomplishments": ["Identified and stayed on track regarding budget and growth projection for a startup company.",
	                    "Implemented a trained computer vision identification model into a pre-existing process flow and server that allowed for $27M funding round for a startup followed by training a team to maintain it and improve it.",
	                    "Refined CRM processes doubling staff productivity while reducing errors when training new employees.",
	                    "Created labor saving solutions without reduction of product or service quality.",],
	"prof_exps": job_array,
	"qualifications": qual_array,
}

resume.render(context)
resume.save("./my_jinga.docx")