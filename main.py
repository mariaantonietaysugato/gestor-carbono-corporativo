from modelos import Empresa, Departamento, ConsumoEnergetico, Transporte, Residuos

def main():
    print("=== INICIALIZANDO GESTOR DE CARBONO CORPORATIVO ===")

    empresa = Empresa("Ecotech Solutions S.A. de C.V.", "ECO123456789")

    dep_operaciones = Departamento("Operaciones", "Jenny Rivera")
    dep_logistica = Departamento("Logística", "Justin Bieber")

    dep_operaciones.agregar_actividad(ConsumoEnergetico("2026-10-01", "Jenny R.", 1500.0))
    dep_operaciones.agregar_actividad(Residuos("2026-10-05", "Jenny R.", 320.0))
    dep_logistica.agregar_actividad(Transporte("2026-10-03", "Justin B.", 2400.0))

    empresa.registrar_departamento(dep_operaciones)
    empresa.registrar_departamento(dep_logistica)

    print(f"\nEmpresa: {empresa.nombre} (RFC: {empresa.rfc})")
    print("-" * 50)

    for dep in empresa.obtener_departamentos():
        print(f"• Departamento: {dep.nombre} | Responsable: {dep.responsable}")
        print(f"  Huella total: {dep.calcular_huella_departamento():.2f} kg CO2e\n")

    print("=" * 50)
    print(f"HUELLA TOTAL EMPRESA: {empresa.calcular_huella_total():.2f} kg CO2e")

if __name__ == "__main__":
    main()