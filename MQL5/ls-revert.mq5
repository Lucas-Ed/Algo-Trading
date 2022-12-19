//+------------------------------------------------------------------+
//|                                                          buy.mq5 |
//|                                   Copyright 2022, Lucas Eduardo. |
//|                       https://www.mql5.com/pt/users/lucas_tranpo |
//+------------------------------------------------------------------+
#include <metatrader5/MT5.mqh>
#include <time.mqh>

//+------------------------------------------------------------------+
//| Script program start |
//+------------------------------------------------------------------+

string ativo_A = "EURUSD"; // Definir os ativos
string ativo_B = "GBPUSD";

if (!MT5::Initialize()) // Conecte-se ao servidor MetaTrader 5
{
    printf("Não foi possível inicializar o MetaTrader5");
    MT5::Shutdown();
    return;
}

void VerificarOrdens()
{
    // Verifique se há ordens abertas para os ativos
    MT5::Orders ordens_abertas_A = MT5::Orders::Get(ativo_A);
    MT5::Orders ordens_abertas_B = MT5::Orders::Get(ativo_B);

    // Se houver ordens abertas para os ativos, pergunte ao usuário se deseja enviar ordens de compra/venda
    if (ordens_abertas_A.Total() || ordens_abertas_B.Total())
    {
        string resposta = InputString("Deseja enviar as ordens BUY/SELL ? (S/N)");
        if (resposta == "S")
        {
            // Reverta as ordens abertas para os ativos simultaneamente
            for (int i = 0; i < ordens_abertas_A.Total(); i++)
                MT5::Order::Close(ordens_abertas_A[i]);
            for (int i = 0; i < ordens_abertas_B.Total(); i++)
                MT5::Order::Close(ordens_abertas_B[i]);
            printf("Ordens executadas com sucesso !!!");
        }
        else
        {
            printf("Erro ao executar as ordens");
        }
    }

    // Se não houver ordens abertas, pergunte ao usuário se deseja encerrar o algoritmo
    else
    {
        string resposta = InputString("Deseja encerrar o algoritmo ? (S/N)");
        if (resposta == "S")
        {
            printf("Encerrando algoritmo em 10 segundos....");
            Sleep(10000);
            MT5::Shutdown();
        }
        else
        {
            printf("Reiniciando algoritmo em 10 segundos....");
            Sleep(10000);
            VerificarOrdens();
        }
    }
}

// Verifique as ordens novamente
VerificarOrdens();

// Desconecte-se do servidor
class MinhaClasse
{
public:
    void DesconectarServidor()
    {
        if (MT5::IsConnected()) // Verifique se o algoritmo está conectado ao servidor
        {
            MT5::Shutdown(); // Desconecte o algoritmo do servidor
            printf("Desconectado do servidor com sucesso");
        }
        else
        {
            printf("Ocorreu um errro ao desconectar !!!");
        }
    }
};

MinhaClasse classe;
classe.DesconectarServidor();
