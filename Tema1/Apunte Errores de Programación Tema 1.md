# Errores de programación
## 1. Error de Redondeo Binario
El error más común es intentar representar números decimales exactos (como 0.1) en un sistema binario. Esto causa que operaciones simples devuelvan resultados inesperados.
- Ejemplo:
  - System.out.println (0.1 + 0.2); //imprime 0.30000000000000004 en lugar de 0.3.
- Causa: Fracciones decimales no tienen una representación binaria finita.


## 2. Pérdida de Precisión por Magnitud(IEEE 754 )
Cuando se operan números con magnitudes muy diferentes, el número más pequeño puede &quot;desaparecer&quot; debido a que no cabe en la mantisa del número más grande. 
- Ejemplo: Sumar 1.0 a un double extremadamente grande puede no cambiar el valor original.

## 3. Comparación Directa con ==
Debido a los errores de redondeo mencionados, comparar dos números double usando == suele fallar.
- Solución: Se debe usar un margen de error (épsilon).

>java

`if (Math.abs(a - b) &lt; 0.00001) { /* son iguales */ }`

## 4. Acumulación de Errores en Bucles

Realizar miles de operaciones aritméticas consecutivas con double acumula pequeños errores de redondeo que pueden resultar en una desviación significativa al final del proceso.

## 5. Cancelación por Resta (Loss of Significance)

Ocurre cuando restas dos números muy cercanos entre sí. La mayoría de los dígitos significativos se cancelan, dejando solo el error de redondeo como el &quot;resultado&quot; aparente.

## 6. Desbordamiento Silencioso (Overflow)

A diferencia de los errores de decimales, este ocurre con tipos enteros (int, long). Si
superas el valor máximo, Java no lanza una excepción; simplemente &quot;da la vuelta&quot; al
número más pequeño (negativo), lo que destruye la exactitud del cálculo. 
java
public class DesbordamientoEntero {
    public static void main(String[] args) {
        int max = Integer.MAX_VALUE; // 2,147,483,647
        int resultado = max + 1;
        System.out.println(&quot;Máximo int: &quot; + max);
        System.out.println(&quot;Máximo + 1: &quot; + resultado); // Imprime -2147483648
        // Solución: Usar Math.addExact para lanzar una excepción si ocurre
        try {
            Math.addExact(max, 1);
        } catch (ArithmeticException e) {
            System.out.println(&quot;Error detectado: ¡Desbordamiento!&quot;);
        }
    }
}

Conversión Estrecha (Narrowing Primitive Conversion)

Al convertir un tipo de mayor capacidad a uno menor (de double a int o de long a int),
Java simplemente trunca los bits sobrantes, lo que puede cambiar drásticamente el
valor original sin previo aviso. 
Java

public class ErrorConversion {
    public static void main(String[] args) {
        double valorDouble = 3.14159e10; // Un número muy grande
        int valorInt = (int) valorDouble; // Casting explícito
        System.out.println(&quot;Valor Original: &quot; + valorDouble);
        System.out.println(&quot;Valor Truncado: &quot; + valorInt);
        // Imprime 2147483647 (el máximo int) porque el double no cabe.
    }
}

ADD

Error por División Entera
Cuando se dividen dos números enteros, Java descarta la parte decimal, aunque el
resultado se asigne a un double.
• Ejemplo: 5 / 2 produce 2 en lugar de 2.5
• Causa: Ambos operandos son enteros, por lo que se aplica división entera.
public class DivisionEntera {
    public static void main(String[] args) {
        int a = 5;
        int b = 2;
        double resultado = a / b; // División entera antes de asignar
        System.out.println(&quot;Resultado incorrecto: &quot; + resultado);
        // Solución
        double resultadoCorrecto = (double) a / b;
        System.out.println(&quot;Resultado correcto:   &quot; + resultadoCorrecto);
    }
}
Uso Incorrecto de Math.pow con Enteros
Math.pow devuelve un double, lo que puede causar errores de precisión o casting
inesperado.
• Ejemplo: Elevar potencias para cálculos exactos
• Causa: Conversión implícita de double a int
public class ErrorMathPow {
    public static void main(String[] args) {
        int resultado = (int) Math.pow(2, 31);
        System.out.println(&quot;Resultado: &quot; + resultado);
        // Valor incorrecto por desbordamiento y conversión
    }
}

Uso Incorrecto de String == String

Comparar cadenas con == compara referencias, no el contenido.
• Ejemplo: Dos textos iguales pueden evaluarse como diferentes
• Causa: == compara direcciones de memoria
public class ComparacionString {
    public static void main(String[] args) {
        String a = new String(&quot;Hola&quot;);
        String b = new String(&quot;Hola&quot;);
        if (a == b) {
            System.out.println(&quot;Son iguales&quot;);
        } else {
            System.out.println(&quot;SON DIFERENTES (Error)&quot;);
        }
        // Solución correcta
        if (a.equals(b)) {
            System.out.println(&quot;Son iguales usando equals()&quot;);
        }
    }
}
NullPointerException (Error Más Común)
Ocurre al intentar usar un objeto que no ha sido inicializado.
• Ejemplo: Llamar métodos sobre null
• Causa: Falta de validación
public class ErrorNullPointer {
    public static void main(String[] args) {
        String texto = null;
        System.out.println(texto.length()); // Excepción en tiempo de ejecución
    }
}

Índice Fuera de Rango (ArrayIndexOutOfBoundsException)
Acceder a una posición inexistente de un arreglo.

• Ejemplo: Acceder más allá del tamaño
• Causa: Error lógico en índices
public class ErrorIndiceArreglo {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3};
        System.out.println(numeros[3]); // Índice inválido
    }
}

Bucle Infinito Accidental
Ocurre cuando la condición de salida nunca se cumple.
• Ejemplo: Contador que no cambia correctamente
• Causa: Error lógico

public class BucleInfinito {
    public static void main(String[] args) {
        int i = 0;
        while (i &lt; 5) {
            System.out.println(&quot;i = &quot; + i);
            // Falta i++
        }
    }
}
