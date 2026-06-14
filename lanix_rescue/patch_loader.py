import sys

def patch_loader():
    try:
        with open('official_loader.bin', 'rb') as f:
            loader = f.read()
        with open('ddr_1332.bin', 'rb') as f:
            old_ddr = f.read()
        with open('ddr_1056.bin', 'rb') as f:
            new_ddr = f.read()

        if len(old_ddr) != len(new_ddr):
            print(f"❌ ERROR: Los tamaños no coinciden ({len(old_ddr)} vs {len(new_ddr)}).")
            sys.exit(1)

        if old_ddr in loader:
            print("✅ Blob de 1332MHz encontrado dentro del loader oficial.")
            patched_loader = loader.replace(old_ddr, new_ddr, 1) # Reemplazar solo la primera coincidencia
            
            with open('patched_loader.bin', 'wb') as f:
                f.write(patched_loader)
            print("✅ Loader parcheado guardado como 'patched_loader.bin'")
        else:
            print("❌ ERROR: No se pudo encontrar el blob de 1332MHz dentro del loader.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error de Python: {e}")
        sys.exit(1)

if __name__ == "__main__":
    patch_loader()
