# Follow these steps to deploy a pipeline using Git actions

## 1. Deploying through Github generates git action in your repository

## 2. Deploying through Azure repos will create pipelines in Azure DevOps

## 3. Create Database in Azure

## 4. Update settings.py in the project level of the Django app with the credentials of the database

## 5. Create Webapp using Azure

## 6. Click browse

## 7. Go to deployment slot in the blade of the web app in Azure portal

## 8. Configure GitHub or Azure Repos(Azure DevOPs) to connect with your repo to build the yaml file

## 9. Save configurations

## 10. Go to App Service logs and click on File System and Save

## 11. Use bash command *```pip freeze > requirements.txt```* to push all your dependencies to the same file name created in the root of the project folder

## 12. Make sure ALLOWED_HOST = ["*"] in settings.py to make the address of the webapp….. azure.net work

  Normally you should specify the ipaddress of your webapp only in this area.
  
## 13. Create an Application Setting with the following configs under "your-webapp">Configuration

| Name:  |DATABASE_URL                                                                        |
|--------|----------------------------------------------------------------------------------------|
| Value: | postgresql://postgres:password@yourdjangoapp.postgres.database.azure.com:5432/postgres |
| a.     | postgres username                                                                      |
| b.     | postgres password                                                                      |
| c.     | postgres host                                                                          |
| d.     | postgres port                                                                          |
| e.     | postgres database name                                                                 |
  
    |postgresql://"a":"b"@"c":"d"/"e'|

## 14. Check if the build is successful
