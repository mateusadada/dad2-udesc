/*
Crie um outro programa em JAVA agora utilizando Hashtable, que armazene o nome dos estados utilizando como chave sua respectiva sigla
- Execute a mesma sequência de testes feita para o primeiro exercício (exercise_014)

- Tente inserir um par chave-valor duplicado, p. ex.: Santa Catarina, e veja o resultado

- Inclua sua análise comparativa, do Hashtable com o HashMap, no corpo do programa como comentário
*/

package exercise_015;

import java.util.Hashtable;
import java.util.Map;

public class exercise_015 {
    public static void main(String[] args) {
        Map<String, String> estados = new Hashtable<>();

        estados.put("SC", "Santa Catarina");
        estados.put("RJ", "Rio de Janeiro");
        estados.put("SP", "São Paulo");
        estados.put("PR", "Paraná");
        estados.put("RS", "Rio Grande do Sul");

        System.out.println("Conteúdo da tabela usando keySet():");
        for (String sigla : estados.keySet()) {
            System.out.println(sigla + ": " + estados.get(sigla));
        }

        System.out.println("\nA ordem dos dados mostrados é a mesma da sequência de inserção? "
                + (estados.keySet().toString().equals("[SC, RJ, SP, PR, RS]") ? "Sim" : "Não"));

        String resultado = estados.put("SC", "Santa Catarina");
        System.out.println("\nResultado da tentativa de inserção de um par chave-valor duplicado: " + resultado);

        System.out.println("\nPares chave-valor usando values():");
        for (String valor : estados.values()) {
            System.out.println(valor);
        }

        /*
        Hashtable é sincronizado, garantindo segurança em ambientes multi-threaded, enquanto HashMap não é,
        proporcionando melhor desempenho em ambientes single-threaded. Hashtable não permite chaves ou valores nulos,
        ao contrário de HashMap, que os aceita, tornando a escolha entre eles dependente das necessidades de sincronização e manipulação de nulos.
        */
    }
}
