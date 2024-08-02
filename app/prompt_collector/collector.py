class Collector:
    def __init__(self, heading: str, footer: str):
        self.__context_heading = heading
        self.__context_footer = footer
    
    def collect_value(self, value_to_provide_name: str) -> str:
        while True:
            if self.__context_heading:
                prompt = f'\n{self.__context_heading}\n'
                
            prompt += f'Provide a value for [{value_to_provide_name}] followed by the Enter key'        
            
            if self.__context_footer:
                prompt += f'\n{self.__context_footer}'
                
            response_value = input(prompt).strip()
            if response_value:
                return response_value
            
            retry = input(f'[{value_to_provide_name}] cannot be empty. Do you want to retry? (Y/N): ').strip()
            if retry == 'n':
                print('Input process cancelled')
                exit()