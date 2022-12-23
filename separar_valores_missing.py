def separar_valores_missing (nomeDataframe):
    
    '''
    LEGENDA:
    nomeDataframe - Significa o Nome do Dataframe
    '''
    
    # importar biblioteca
    import pandas as pd
    
#################################### Selecao Dataframe ####################################
    
    # Selecionar Dataframe    
    df_dados = nomeDataframe    

#################################### Separacao Dados Missing ####################################    
    
    # Separar Missing
    missing = df_dados[df_dados.isnull().any(axis = 1)]
      
#################################### Index Dados Missing ####################################    
    
    # Index Missing
    index_list = missing.index.values 
        
#################################### Deletar Missing Dataframe ####################################    
    
    # Deletar dados do Dataframe através do Índice
    sem_missing = df_dados.drop(labels= index_list, axis= 0)
        
#################################### Salvar Dataframes ####################################    
    
    # Gerar arquivo csv sem índice e com outros separadores (ponto e vírgula)
    missing.to_csv('missing.csv', index = True)
    sem_missing.to_csv('database.csv', index = False)   
    
#################################### Exibicao Info ####################################
      
    print('ATENÇÃO:')
    print('Arquivos (missing.csv e database.csv) salvos na mesma pasta na qual está o arquivo com extensão .ipynb')
    print('')
    
    print('\n RESUMO INFORMATIVO')    
    missing_values_count = missing.isnull().sum()
    total_missing = missing_values_count.sum()
    total_linhas = df_dados.shape[0]
    missing = missing.shape[0]
    sem_missing = sem_missing.shape[0]

    print('Índice Dados Missing:')

    print('')

    print(index_list)

    print('')

    print('------------------------------------------------------------------------')

    print('Total de Missing: %.0f' % total_missing)
    print('nº Total de linhas: %.0f' % total_linhas)
    print('nº de linhas de Dados Missing: %.0f' % missing)
    print('nº de linhas Sem Dados Missing: %.0f' % sem_missing)
    
#################################### Modulo ####################################    
    
    return (nomeDataframe)