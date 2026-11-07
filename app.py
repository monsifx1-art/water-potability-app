import streamlit as st

# عنوان التطبيق
st.title("🧪 Contrôle de Potabilité de l'Eau")
st.write("Entrez les paramètres physico-chimiques pour vérifier la conformité de l'eau.")

# عناصر الإدخال التفاعلية
ph = st.number_input("Entrer la valeur de pH :", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
n = st.number_input("Entrer la valeur de Nitrates (mg/L) :", min_value=0.0, value=10.0, step=1.0)
c = st.number_input("Entrer la valeur de Conductivité (µS/cm) :", min_value=0.0, value=500.0, step=10.0)

# زر التحليل
if st.button("Vérifier la conformité"):
    st.subheader("--- Résultats ---")
    
    # التحقق من الشروط
    is_ph_ok = 6.5 <= ph <= 8.5
    is_n_ok = n <= 50
    is_c_ok = c <= 1000  # يمكنك تعديل المعيار حسب الحاجة

    if is_ph_ok and is_n_ok and is_c_ok:
        st.success("✅ Eau conforme aux normes.")
    else:
        st.error("❌ Eau non conforme :")
        if not is_n_ok:
            st.warning(f"- Nitrates non conformes ({n} mg/L > 50 mg/L)")
        if not is_c_ok:
            st.warning(f"- Conductivité non conforme ({c} µS/cm)")
        if not is_ph_ok:
            st.warning(f"- pH non conforme ({ph})")
