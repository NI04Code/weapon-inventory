Naufal Ichsan - 2206082013 
PBP Tugas 2
**Step by Step**
1. Membuat sebuah proyek Django baru.  
        1. Membuat direktori baru bernama weapon_inventory.  
        2. Menginisiasi virtual environment yang saya beri nama env dan mengaktifkannya dengan command  
           'source env/bin/ activate'      
        3. Melakukan download seluruh dependencies termasuk django itu sendiri      
           melalui requirements.txt menggunakan pip didalam virtual environment     
        4. Menggunakan command 'django-admin startproject weapon_inventory .' untuk menginisasi      
           project django baru bernama weapon_inventory      
2. Membuat aplikasi dengan nama main pada proyek tersebut.     
        1. Menggunakan command 'python3 manage.py startapp weapons --> saya memberi nama app saya weapons bukan main,    
           menurut saya nama ini lebih cocok untuk membuat sebuah weapon inventory      
        2. Saya mendaftarkan app weapons kedalam settings --> INSTALLED APPS yang ada pada projek weapon_inventory     
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.     
        1. Saya membuat file urls.py pada app weapons terlebih dahulu       
        2. Saya mengimpor include pada urls.py pada proyek untuk memasukkan urls pada aplikasi weapons pada list urlpattern
           Syntax saya gunakan adalah 'path('', include('weapons.urls'))' --> pada syntax terdapat 'path('', url) disini saya   beri string kosong agar app langsung keredirect ke weapons.views ketika link diklik   
4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.   
   name sebagai nama item dengan tipe CharField.   
   amount sebagai jumlah item dengan tipe IntegerField.   
   description sebagai deskripsi item dengan tipe TextField.   
        1. Saya melakukan import models dari django.db   
        2. Saya membuat class Weapon yang isinya adalah atribut seperti diatas   
        3. Saya menambahkan beberapa attributes seperti atk, critrate, dan critdmg yang menurut saya relevan dengan     
           weapons attributes      
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta     
   nama dan kelas kamu.    
        1. Saya membuat folder templates terlebih dahulu yang isinya merupakan template html yang saya beri nama    
           weapons.html untuk menampilkan apa yang ada di views    
        2. Saya melakukan import render dari django.shortcut pada views.py dan membuat function show_weapons yang berfungsi   
           menampilkan weapons weapons yang ada    
        3. Di dalam Function saya membuat suatu dict yang berisi key berdasarkan models yang sudah dibuat dan valuenya.   
        4. Setelahnya, saya melakukan return kepada weapons.html agar data yang ada di views dapat ditampilkan oleh html   
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.   
        1. saya membuat berkas urls.py pada direktori weapons yang nantinya akan disi urlpatterns juga, nantinya urlpatterns    
           ini akan diarahkan ke fungsi show_weapons yang ada pada weapons.views   
7.  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh    
    teman-temanmu melalui Internet.   
        1. Melakukan deploy ke adaptable seperti pada tutorial 0 yang membedakan adalah pada start command diberikan perintah   
           'python manage.py migrate && gunicorn weapon_inventory.wsgi' agar mengarah ke wsgi weapon_inventory   

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**        

   Request              urls.py               views.py           models.py           Templates   
     ↓                    ↓                      ↓                   ↓                   ↓
   Client  ────────>   URL Dispatcher  ──────>   Views  ──────>   Models  ──────>   HTML   
          <────────  HTTP Response   <───────   <──────────   <──────────   <──────────   

Request dari Client: Permintaan HTTP pertama kali diterima dari klien oleh Django.   

**URL Dispatcher (urls.py)**: Berkas urls.py mencocokkan URL yang diterima dari klien dengan pola URL yang ada dan mengarahkannya ke view yang sesuai.

**Views (views.py)**: Views adalah tempat logika aplikasi terletak. views.py menerima permintaan dari URL Dispatcher, memprosesnya, dan menyiapkan data yang akan ditampilkan oleh template.

**Models (models.py)**: Models mengelola struktur dan logika data. models.py berinteraksi dengan database sql dan memungkinkan views untuk mengambil atau menyimpan data.

**Templates (HTML)**: Templates adalah file HTML yang digunakan untuk merender tampilan akhir yang akan ditampilkan kepada klien. Mereka mengambil data dari views.py melalui template engine Django.

**HTTP Response ke Client**: Hasil akhir dalam bentuk HTTP Response dikirim kembali ke klien untuk ditampilkan sebagai output.


**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment biasa kita gunakan dalam pengembangan perangkat lunak, termasuk dalam pengembangan aplikasi web berbasis Django, dengan tujuan utama diantaranya:

1. **Isolasi Lingkungan:** Virtual environment memungkinkan kita untuk membuat lingkungan pengembangan yang terisolasi. Setiap virtual environment memiliki lingkungan yang terpisah dari interpreter Python dan library yang dibutuhkan. Ini memungkinkan kita mengelola dependensi proyek yang ingin dilakukan secara terpisah dan menghindari konflik antara versi library yang berbeda yang mungkin dibutuhkan oleh berbagai proyek Anda.

2. **Manajemen Dependensi:** Dengan virtual environment, kita dapat mengelola dependensi proyek dengan lebih baik. Kita dapat menggunakan pip untuk menginstall, mengupgrade, atau menghapus library tertentu hanya dalam lingkungan virtual proyek Anda, tanpa mempengaruhi Python atau proyek lain yang berjalan di lingkungan yang berbeda.

3. **Versi Python yang Berbeda:** Jika kita memiliki banyak proyek yang memerlukan versi Python yang berbeda, kita dapat dengan mudah membuat virtual environment yang sesuai dengan versi Python yang diperlukan untuk setiap proyek.

4. **Keamanan Proyek:** Isolasi dengan virtual environment dapat membantu mengurangi risiko memengaruhi proyek lain ketika kita menginstall atau mengupgrade library yang diinginkan oleh salah satu proyek. Hal ini membantu menjaga stabilitas dan keamanan proyek-proyek tersebut.

5. **Mudah Dipindahkan:** Virtual environment adalah lingkungan yang dapat dibuat, disalin, dan dipindahkan dengan mudah. Ini memudahkan kita untuk berbagi proyek dengan developer lain atau menjalankannya di lingkungan/directory yang berbeda.

Django sendiri dapat dijalankan tanpa adanya virtual environment. Namun, ini bukan best practice dan dapat menyebabkan beberapa masalah, terutama ketika kita bekerja pada beberapa proyek atau jika kita mau mengelola dependensi dengan baik. Menggunakan virtual environment akan membantu kita menghindari potensi masalah konflik dependensi dan memungkinkan kita untuk mengisolasi setiap proyek dengan lebih baik.


**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
MVC, MVT, dan MVVM adalah tiga pola arsitektur perangkat lunak yang umum digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi web. Masing-masing memiliki tujuan dan konsep yang berbeda. Di bawah ini saya akan menjelaskan masing-masing pola tersebut beserta perbedaannya yang saya dapatkan dari berbagai sumber:

1. **MVC (Model-View-Controller):**
   - **Model** merupakan komponen yang bertanggung jawab untuk mengelola logika dan data aplikasi. Model mengurus akses ke database atau penyimpanan data, serta menjalankan operasi operasi tertentu.
   - **View** merupakan komponen yang bertanggung jawab untuk menampilkan data kepada pengguna. Tampilan mengambil informasi dari Model dan menampilkan tampilan yang sesuai untuk pengguna.
   - **Controller** merupakan komponen yang bertindak sebagai perantara antara Model dan View. Ini menerima input dari pengguna, memprosesnya, dan mengubah Model atau tampilan sesuai dengan input tersebut.

   **Perbedaan Utama:** MVC memisahkan aplikasi menjadi tiga komponen utama (Model, View, Controller) untuk mengelola tanggung jawab dan logika aplikasi. Ini adalah pola yang paling umum digunakan dalam pengembangan aplikasi web.

2. **MVT (Model-View-Template):**
   - **Model** seperti dalam MVC, Model bertanggung jawab atas logika dan akses ke data.
   - **View** dalam MVT mirip dengan View dalam MVC, bertanggung jawab untuk tampilan yang diberikan kepada pengguna.   
   - **Template** merupakan komponen yang memproses tampilan dan mengisi data dari Model ke dalam tampilan sebelum mengirimkannya ke pengguna.

   **Perbedaan Utama:** MVT adalah varian dari MVC yang digunakan dalam kerangka kerja Django, yang biasanya digunakan untuk pengembangan web. Perbedaan utamanya adalah adanya Template yang bertanggung jawab untuk memproses tampilan, sementara dalam MVC, tampilan biasanya diolah oleh View.

3. **MVVM (Model-View-ViewModel):**
   - **Model** seperti dalam MVC dan MVT, Model mengurus data dan logika.
   - **View** merupakan tampilan yang diberikan kepada pengguna, seperti dalam pola MVC dan MVT.
   - **ViewModel** merupakan komponen yang menghubungkan Model dan View. Ini berisi logika tampilan dan berfungsi sebagai perantara antara Model dan View. ViewModel sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile.

   **Perbedaan Utama:** MVVM adalah pola arsitektur yang lebih khusus digunakan dalam pengembangan antarmuka pengguna. ViewModel bertindak sebagai perantara antara Model dan View, memisahkan tampilan dan logika dengan baik. Ini sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang kompleks.

Saat memilih pola arsitektur untuk proyek, penting untuk mempertimbangkan kebutuhan proyek dan jenis aplikasi yang Anda kembangkan. MVC dan MVT adalah pilihan umum untuk pengembangan web, sedangkan MVVM lebih umum digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna. Setiap pola memiliki kelebihan dan kelemahan sendiri, dan pilihan terbaik tergantung pada konteks proyek yang dikerjakan.

