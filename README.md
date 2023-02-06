# RSA Signature Generator/Verifier (no Crypto packages)

Author: Felipe Nacimento Rocha


        1. Parte I: Geração de chaves e cifra
        
                a. Geração de chaves (p e q primos com no mínimo de 1024 bits) (DONE)
                b. Cifração/decifração assimétrica RSA usando OAEP.  (DONE)
    
    
        2.  Parte II: Assinatura
        
                a. Cálculo de hashes da mensagem em claro (função de hash SHA-3) (DONE)
                b. Assinatura da mensagem (cifração do hash da mensagem) (DONE)
                c. Formatação do resultado (caracteres especiais e informações para verificação em BASE64)
        
        
        3. Parte III: Verificação:
        
                a. Parsing do documento assinado e decifração da mensagem (de acordo com a formatação usada, no caso BASE64) 
                b. Decifração da assinatura (decifração do hash) (DONE)
                c. Verificação (cálculo e comparação do hash do arquivo) (DONE)


#### Execução:
Python >=3.10


```
        python main.py
```

