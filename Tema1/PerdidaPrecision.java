public class PerdidaPrecision {
    public static void main(String[] args) {
        // Un double tiene aproximadamente 15-17 dígitos significativos de precisión
        double numeroGrande = 1.0e16; // 1 seguido de 16 ceros
        double numeroPequeno = 1.0;
        double resultado = numeroGrande + numeroPequeno;
        System.out.println("--- Demostración de Pérdida de Precisión ---");
        System.out.println("Número Grande:  " + numeroGrande);
        System.out.println("Número Pequeño: " + numeroPequeno);
        System.out.println("Suma Resultante: " + resultado);
        // Verificación lógica
        if (resultado == numeroGrande) {
            System.out.println("\nRESULTADO: El número pequeño 'desapareció'.");
            System.out.println("La suma es igual al número original debido a la falta de bits en la mantisa.");
        }
        // --- SOLUCIÓN USANDO BIGDECIMAL ---
        java.math.BigDecimal bdGrande = new java.math.BigDecimal("1.0e16");
        java.math.BigDecimal bdPequeno = new java.math.BigDecimal("1.0");
        java.math.BigDecimal bdResultado = bdGrande.add(bdPequeno);
        System.out.println("\n--- Solución con BigDecimal ---");
        System.out.println("Suma Exacta:   " + bdResultado.toPlainString());
    }
}
