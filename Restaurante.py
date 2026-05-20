# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Solución Problema 2: Gestión de Precios de Menú de Restaurante
# Nombre del estudiante: Johan Felipe Roncancio Guzman
# =====================================================================

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral):
    """
    Determina el precio final de un producto aplicando un 15% de descuento
    si pertenece a la categoría objetivo y supera el umbral de precio configurado.
    """
    if categoria_producto == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        return precio_base


def main():
    print("====================================================")
    print("      SISTEMA DE GESTIÓN DE PRECIOS - RESTAURANTE   ")
    print("====================================================")
    
    
    menu_restaurante = [
        ["Hamburguesa Gourmet", "Comida Rápida", 25000],
        ["Papas Nativas", "Comida Rápida", 8000],
        ["Limonada Natural", "Bebidas", 7500],
        ["Jugo de Mandarina", "Bebidas", 9500],
        ["Tres Leches", "Postres", 12000],
        ["Brownie con Helado", "Postres", 10500]
    ]
    
 
    categoria_promocion = "Bebidas"
    umbral_precio = 8000
    
    print(f"Promoción: 15% desc. en '{categoria_promocion}' con precio mayor a ${umbral_precio:,}")
    print("====================================================\n")
    
    print(f"{'PRODUCTO':<23} | {'CATEGORÍA':<15} | {'PRECIO BASE':<13} | {'PRECIO FINAL':<13}")
    print("-" * 73)
    
   
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
      
        precio_final = calcular_precio_final(categoria, precio_base, categoria_promocion, umbral_precio)
        
        print(f"{nombre:<23} | {categoria:<15} | ${precio_base:<12,} | ${precio_final:<12,.2f}")
        
    print("-" * 73)

if __name__ == "__main__":
    main()