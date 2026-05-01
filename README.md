# remarcable-demo
Demo application created for Remarcable using Django

# Setup Instructions:
1. Clone the repository
2. Navigate to project directory and install dependencies using prefered package manager
	* for pip: ```pip install .```
4. Navigate to the main remarcable directory containaing manage.py
	* run: ```python manage.py runserver``` to start the development server

Assumptions:
- Each product can have multiple tags and multiple categories
- Product can be searched by both description and title fields


ER Diagram:

```mermaid
erDiagram
	direction TB
	PRODUCT {
		bigint id PK ""  
		string name  ""  
		string description  ""  
		float price  ""  
		category category FK ""  
	}

	TAG {
		bigint id PK ""  
		string tag_name  ""  
	}

	CATEGORY {
		bigint id PK ""  
		string category_name  ""  
	}

	PRODUCT_TAG {

	}

	PRODUCT_CATEGORY {

	}

	PRODUCT||--o{PRODUCT_TAG:"  "
	CATEGORY||--o{PRODUCT_CATEGORY:"  "
	TAG||--o{PRODUCT_TAG:"  "
	PRODUCT_CATEGORY}o--||PRODUCT:"  "
```
