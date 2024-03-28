/*
Crie um programa em JAVA que armazene em uma tabela com HashMap o nome dos estados na seguinte ordem:
Santa Catarina; Rio de Janeiro; São Paulo; Parana; e Rio Grande do Sul

- Utilize como chave a sigla do estado (SC, RJ, SP, PR e RS)

- Mostre na tela o conteúdo da tabela utilizando os métodos get() e keySet()
    - Verifique se a ordem dos dados mostrados é a mesma da sequencia em que foram inseridos

- Insira um par chave-valor primeiro com o valor nulo, depois tente com a chave nula
    - Verifique se esta inserção é aceita e se todos os pares são apresentados com o método values()
*/

package exercise_014;

import java.util.HashMap;
import java.util.Map;

public class exercise_014 {
    public static void main(String[] args) {
        Map<String, String> estados = new HashMap<>();

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

        estados.put(null, "Valor nulo");
        estados.put("NU", null);

        System.out.println("\nPares chave-valor usando values():");
        for (String valor : estados.values()) {
            System.out.println(valor);
        }
    }
}
