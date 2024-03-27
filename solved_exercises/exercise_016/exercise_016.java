/*
Teste um dos exercícios (usado o exercise_014) com a interface Iterator.
*/

package exercise_016;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class exercise_016 {
    public static void main(String[] args) {
        Map<String, String> estados = new HashMap<>();

        estados.put("SC", "Santa Catarina");
        estados.put("RJ", "Rio de Janeiro");
        estados.put("SP", "São Paulo");
        estados.put("PR", "Paraná");
        estados.put("RS", "Rio Grande do Sul");

        System.out.println("Conteúdo da tabela usando Iterator:");
        Iterator<String> iterator = estados.keySet().iterator();
        while (iterator.hasNext()) {
            String sigla = iterator.next();
            System.out.println(sigla + ": " + estados.get(sigla));
        }

        System.out.println("\nA ordem dos dados mostrados é a mesma da sequência de inserção? "
                + (estados.keySet().toString().equals("[SC, RJ, SP, PR, RS]") ? "Sim" : "Não"));

        estados.put("SC", "Santa Catarina");

        System.out.println("\nPares chave-valor usando values():");
        for (String valor : estados.values()) {
            System.out.println(valor);
        }
    }
}
