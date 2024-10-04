import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

df = pd.read_csv("bike_clean_fix.csv")

st.title('Proyek Analisis Data: Bike Sharing Dataset')

st.caption('Disusun oleh: Ade Putra Anggoro / m200b4ky0076@bangkit.academy / adeangg / ML-42')

st.subheader('Dataset Daily Bike')
st.dataframe(data=df, width=750, height=200)

st.header('1. Komparasi Penyewa Tipe Casual dan Registered')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.subheader("Total Sewa Per Tahun")
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(16, 12))
        sns.barplot(data=df, x='yr', y='cnt', estimator=sum, palette='Blues', ax=ax)
        ax.set_title("Total Sewa Sepeda Berdasarkan Tahun (2011-2012)", loc="center", fontsize=30)
        ax.set_ylabel('Total Sewa Sepeda', fontsize=15)
        ax.set_xlabel('Tahun', fontsize=15)
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=15)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(16, 12))
        sns.barplot(x='yr', y='registered', data=df, label='Registered Users', color='green', ax=ax)
        sns.barplot(x='yr', y='casual', data=df, label='Casual Users', color='yellow', ax=ax)
        ax.set_title('Korelasi Registered dan Casual', loc="center", fontsize=30)
        ax.set_xlabel('Year', fontsize=15)
        ax.set_ylabel('Rata-Rata Pengguna', fontsize=15)
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=15)
        ax.legend(fontsize="20")
        st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            1. Terdapat peningkatan yang cukup signifikan dalam jumlah total penyewaan
            sepeda pada tahun 2012 dibandingkan dengan tahun 2011.
            Ini mengindikasikan adanya pertumbuhan yang pesat dalam penggunaan
            layanan bike sharing selama periode tersebut.
            2. Meskipun tidak sebesar pengguna registered, jumlah pengguna casual juga 
            mengalami peningkatan. Hal ini mengindikasikan bahwa layanan bike sharing 
            semakin populer dan menarik minat orang untuk mencoba layanan ini meskipun belum menjadi anggota.
            Pada kedua tahun, pengguna registered mendominasi jumlah total pengguna. 
            Ini menunjukkan bahwa model bisnis berbasis keanggotaan cukup efektif dalam menarik 
            dan mempertahankan pelanggan.
        ''')
 
with tab2:
    st.subheader("Trend Penyewaan")
    # Create the figure and axes object
    fig, ax = plt.subplots(figsize=(20, 8))
    df_melt = df.melt(id_vars=['dteday'], value_vars=['casual', 'registered'], var_name='User Type', value_name='Count')
    sns.lineplot(data=df_melt, x='dteday', y='Count', hue='User Type', palette='Set2', ax=ax)
    ax.set_title('Perbandingan Pengguna Casual vs Registered', fontsize=16)
    ax.set_xlabel('Tanggal', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            1. Terdapat fluktuasi harian yang signifikan pada jumlah pengguna,
            baik casual maupun registered. Ini menunjukkan adanya faktor-faktor 
            harian yang mempengaruhi keputusan pengguna untuk menyewa sepeda, 
            seperti cuaca, hari kerja, dan acara khusus (dibahas pada pertanyaan no 2).
            2. Ketergantungan pada Cuaca: Fluktuasi harian yang tajam menunjukkan bahwa 
            cuaca memiliki pengaruh yang sangat besar terhadap jumlah penyewaan. 
            Hari-hari yang cerah dan hangat cenderung menarik lebih banyak pengguna 
            (dibahas pada pertanyaan no 2).
        ''')
 
with tab3:
    st.subheader("Total Penyewaan Harian dan Bulanan")
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(16, 12))
        weekday_data = df.groupby('weekday')[['casual', 'registered']].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=weekday_data, x='weekday', y='casual', label='Casual', markers='o', ax=ax)
        sns.lineplot(data=weekday_data, x='weekday', y='registered', label='Registered', markers='o', ax=ax)
        ax.set_title('Comparison of Casual and Registered Users by Weekday', fontsize=16)
        ax.set_xlabel('Weekday', fontsize=12)
        ax.set_ylabel('Total Users', fontsize=12)
        ax.set_xticks(range(7))
        ax.set_xticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
        ax.legend()
        st.pyplot(fig)

    with col2:
        monthly_agg = df.groupby('mnth')[['casual', 'registered']].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        monthly_agg.plot(x='mnth', y=['casual', 'registered'], kind='bar', color=['#990000', '#006c75'], ax=ax)
        ax.set_title('Total Penyewaan Sepeda per Bulan (Pengguna Kasual vs Terdaftar)', fontsize=16)
        ax.set_xlabel('Bulan', fontsize=12)
        ax.set_ylabel('Total Penyewaan', fontsize=12)
        ax.set_xticks(range(12))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'], rotation=45)
        st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            1. Untuk pengguna registered, jumlah pada weekdays lebih tinggi daripada weekend. 
            Berbanding terbalik dengan pengguna casual, pengguna ini lebih banyak menyewa 
            sepeda pada saat weekend. Kemungkinan faktor disebabkan oleh pengguna registered 
            yang memanfaatkan sewa sepeda untuk bekerja di hari kerja, tidak seperti pengguna 
            casual yang lebih sering memakai pada saat weekend untuk bersantai.
            2. Baik pengguna casual maupun registered sama-sama cenderung banyak 
            melakukan sewa pada pertengahan tahun daripada awal/akhir tahun.
        ''')


st.header('2. Analisis Jumlah Penyewa Sepeda Terhadap Musim/Cuaca pada Periode Tertentu')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.subheader("Total Sewa Bulanan dan Pengaruh Suhu (Temp)")
    col1, col2 = st.columns(2)
    with col1:
        df_monthly_cnt = df.groupby('mnth')['cnt'].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df_monthly_cnt.index, df_monthly_cnt.values)
        ax.set_title('Total Sewa Sepeda Bulanan', fontsize=16)
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Total Rentals', fontsize=12)
        ax.set_xticks(df_monthly_cnt.index)
        ax.grid(True)
        st.pyplot(fig)


    with col2:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df, x='mnth', y='temp', estimator='mean', ax=ax)
        ax.set_title('Trend Suhu Rata-Rata per Bulan', fontsize=16)
        ax.set_xlabel('Bulan', fontsize=12)
        ax.set_ylabel('Suhu Rata-Rata', fontsize=12)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'])
        st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            Penggunaan sewa sepeda paling tinggi ada pada bulan ke-5 hingga ke-9. 
            Penggunaan cenderung rendah ketika memasuki akhir-awal tahun. 
            Setelah dikaitkan dengan trend rata-rata suhu/temperature per bulan, 
            terlihat bahwa suhu cukup tinggi di pertengahan tahun yang memungkinkan 
            penyewa untuk bersepeda dengan nyaman.
        ''')


with tab2:
    st.subheader("Total Sewa Menurut Cuaca dan Pengaruh Hum & Windspeed")
    df_grouped = df.groupby(['mnth', 'weathersit'])['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_grouped, x='mnth', y='cnt', hue='weathersit', palette='Set2', marker='o', ax=ax)
    ax.set_title('Total Sewa Sepeda Bulanan Menurut Cuaca', fontsize=16)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Total Bike Rentals', fontsize=12)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.legend(title='Weather Situation')
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        df_grouped_hum = df.groupby(['mnth', 'weathersit'])['hum'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df_grouped_hum, x='mnth', y='hum', hue='weathersit', palette='Set2', marker='o', ax=ax)
        ax.set_title('Rata-rata Humidity Bulanan Menurut Cuaca', fontsize=16)
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Average Humidity', fontsize=12)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        ax.legend(title='Weather Situation')
        st.pyplot(fig)

    with col2:
        df_grouped_windspeed = df.groupby(['mnth', 'weathersit'])['windspeed'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df_grouped_windspeed, x='mnth', y='windspeed', hue='weathersit', palette='Set2', marker='o', ax=ax)
        ax.set_title('Rata-rata Windspeed Bulanan menurut Cuaca', fontsize=16)
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Average Windspeed', fontsize=12)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        ax.legend(title='Weather Situation')
        st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            1. Banyak penyewa melakukan penyewaan sepeda pada saat cuaca cerah berawan, 
            terbukti bahwa sepanjang tahun cuaca cerah berawan selalu yang tertinggi. 
            Ketika dilakukan analisis dengan rata-rata bulanan humidity dan windspeed, 
            cuaca cerah berawan memiliki tingkat yang rendah dibanding cuaca lainnya. 
            Hal ini menandakan bahwa penyewa merasa nyaman bersepeda dengan cuaca cerah berawan.
            2. Sementara itu, cukup jarang terjadi penyewaan sepeda saat cuaca hujan 
            sepanjang tahunnya. Hal ini dibuktikan dengan humidity dan windspeed dari cuaca ini 
            yang cenderung selalu tinggi sepanjang tahunnya. Hal ini mungkin membuat penyewa sepeda 
            enggan untuk bersepeda di cuaca ini.
        ''')


with tab3:
    st.subheader("Tren Total Sewa Menurut Musim dan Pengaruh Trend Suhu (Temp)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x='dteday', y='cnt', estimator='sum', hue='season', ax=ax)
    ax.set_title('Tren Total Sewa Sepeda dari Waktu ke Waktu', fontsize=16)
    ax.set_xlabel('Tanggal', fontsize=12)
    ax.set_ylabel('Total Sewa Sepeda', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)


    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x='dteday', y='temp', hue='season', markers=True, ax=ax)
    ax.set_title('Trend Suhu (temp) dari Waktu ke Waktu', fontsize=16)
    ax.set_xlabel('Tanggal', fontsize=12)
    ax.set_ylabel('Suhu', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    with st.expander("See explanation"):
        st.write('''
            Trend jumlah sewa bergantung pada musim. 
            Jumlah sewa banyak terjadi di musim panas dan gugur pada pertengahan tahun 
            dibanding 2 musim lainnya. Hal ini berhubungan dengan trend temperatur 
            di sepanjang tahun yang juga sejalan dengan jumlah sewa. 
            Temperatur tinggi selalu tercatat di pertengahan tahun (musim panas & gugur), 
            sementara di musim dingin dan semi temperatur rendah. 
            Perbedaan trend temperatur inilah yang mempengaruhi trend jumlah penyewaan sepeda sepanjang tahun.
        ''')

st.header('Kesimpulan')
st.write('''
        1. Secara umum, pengguna registered selalu lebih banyak daripada pengguna casual. 
        Grafik tidak secara langsung menunjukkan seberapa baru pengguna. 
        Namun, dilihat dari trend 2011-2012, terdapat lonjakan pengguna baru 
        (terutama registered) yang dapat diartikan bahwa banyak yang berminat untuk berlangganan sewa sepeda.
        2. Pengguna sepeda lebih sering melakukan sewa di pertengahan tahun 
        berdasarkan dua tipe pelanggan. Hal ini dipengaruhi oleh musim dan cuaca yang sedang berlangsung, 
        di mana musim dan cuaa juga dipengaruhi oleh faktor seperti temp, humidity, dan windspeed.
        3. Pelanggan lebih sering bersepeda pada cuaca cerah berawan tiap bulannya. 
        Hal ini ditunjukkan dengan rata-rata bulanan winddspeed & humidity 
        yang lebih rendah dibanding cuaca lainnya.
        4. Pelanggan lebih sering bersepeda pada musim panas & gugur sepanjang tahun. 
        Hal ini ditunjukkan dengan trend temp yang lebih tinggi pada dua musim tersebut 
        dibanding trend temp pada musim lainnya.
        ''')
