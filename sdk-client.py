from dotenv
import load_dotenvimport osfrom azure.core.credentials 
import AzureKeyCredentialfrom azure.ai.textanalytics 
import TextAnalyticsClient
def main():  
global ai_endpoint   
global ai_key   
try:    
  # Get Configuration Settings
  load_dotenv()    
  ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')     
  ai_key = os.getenv('AI_SERVICE_KEY')  
# Get user input (until they enter "quit") 
  userText =''   
  while userText.lower() != 'quit':    
    userText = input('\nEnter some text ("quit" to stop)\n')      
    if userText.lower() != 'quit':      
      language = GetLanguage(userText)     
      print('Language:', language)  
except Exception as ex:       
  print(ex)def GetLanguage(text): 
    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)  
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)  
# Call the service to get the detected language  
    detectedLanguage = client.detect_language(documents = [text])[0]   
    return detectedLanguage.primary_language.nameif __name__ == "__main__":  
    main()
