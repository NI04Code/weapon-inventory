Naufal Ichsan - 2206082013
PBP Tugas 2
Step by Step
1. Membuat sebuah proyek Django baru.
        1. Membuat direktori baru bernama weapon_inventory
        2. Menginisiasi virtual environment yang saya beri nama env dan mengaktifkannya dengan command 'source env/bin/activate'
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
           Syntax saya gunakan adalah 'path('', include('weapons.urls'))' --> pada syntax terdapat 'path('', url) disini saya beri string kosong agar app langsung keredirect ke weapons.views ketika link diklik
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

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.




Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan dalam pengembangan perangkat lunak, termasuk dalam pengembangan aplikasi web berbasis Django, dengan tujuan utama sebagai berikut:

1. **Isolasi Lingkungan:** Virtual environment memungkinkan Anda membuat lingkungan pengembangan yang terisolasi secara independen. Setiap virtual environment memiliki salinan terpisah dari interpreter Python dan pustaka (library) yang dibutuhkan. Ini memungkinkan Anda mengelola dependensi proyek Anda secara terpisah dan menghindari konflik antara versi pustaka yang berbeda yang mungkin dibutuhkan oleh berbagai proyek Anda.

2. **Manajemen Dependensi:** Dengan virtual environment, Anda dapat mengelola dependensi proyek Anda dengan lebih baik. Anda dapat menggunakan pip (manajer paket Python) untuk menginstal, mengupgrade, atau menghapus pustaka tertentu hanya dalam lingkungan virtual proyek Anda, tanpa mempengaruhi Python atau proyek lain yang berjalan di lingkungan yang berbeda.

3. **Versi Python yang Berbeda:** Jika Anda bekerja pada berbagai proyek yang memerlukan versi Python yang berbeda, Anda dapat dengan mudah membuat virtual environment yang sesuai dengan versi Python yang diperlukan untuk setiap proyek.

4. **Keamanan Proyek:** Isolasi dengan virtual environment dapat membantu mengurangi risiko memengaruhi proyek lain ketika Anda menginstal atau mengupgrade pustaka. Hal ini membantu menjaga stabilitas dan keamanan proyek-proyek tersebut.

5. **Mudah Dipindahkan:** Virtual environment adalah lingkungan yang dapat dibuat, disalin, dan dipindahkan dengan mudah. Ini memudahkan berbagi proyek dengan rekan pengembang atau menjalankannya di lingkungan yang berbeda.

Sementara virtual environment sangat disarankan dalam pengembangan aplikasi web berbasis Django, Anda tetap dapat membuat aplikasi Django tanpa menggunakannya. Namun, ini bukan praktik terbaik dan dapat menghadirkan beberapa masalah, terutama ketika Anda bekerja pada beberapa proyek atau jika Anda perlu mengelola dependensi dengan baik. Menggunakan virtual environment akan membantu Anda menghindari potensi masalah konflik dependensi dan memungkinkan Anda mengisolasi setiap proyek dengan lebih baik. Sebagian besar komunitas pengembang Python, termasuk komunitas Django, sangat mendorong penggunaan virtual environment untuk pengembangan aplikasi Python.


Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah tiga pola arsitektur perangkat lunak yang umum digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi web. Masing-masing memiliki tujuan dan konsep yang berbeda. Di bawah ini saya akan menjelaskan masing-masing pola tersebut beserta perbedaannya:

1. **MVC (Model-View-Controller):**
   - **Model:** Ini adalah komponen yang bertanggung jawab untuk mengelola logika bisnis dan data aplikasi. Model mengurus akses ke database atau penyimpanan data, serta menjalankan operasi operasi bisnis tertentu.
   - **View:** Komponen ini bertanggung jawab untuk menampilkan data kepada pengguna. Tampilan mengambil informasi dari Model dan menampilkan tampilan yang sesuai untuk pengguna.
   - **Controller:** Controller bertindak sebagai perantara antara Model dan View. Ini menerima input dari pengguna, memprosesnya, dan mengubah Model atau tampilan sesuai dengan input tersebut.

   **Perbedaan Utama:** MVC memisahkan aplikasi menjadi tiga komponen utama (Model, View, Controller) untuk mengelola tanggung jawab dan logika aplikasi. Ini adalah pola yang paling umum digunakan dalam pengembangan aplikasi web.

2. **MVT (Model-View-Template):**
   - **Model:** Seperti dalam MVC, Model bertanggung jawab atas logika bisnis dan akses ke data.
   - **View:** View dalam MVT mirip dengan View dalam MVC, bertanggung jawab untuk tampilan yang diberikan kepada pengguna.
   - **Template:** Template adalah komponen yang memproses tampilan dan mengisi data dari Model ke dalam tampilan sebelum mengirimkannya ke pengguna.

   **Perbedaan Utama:** MVT adalah varian dari MVC yang digunakan dalam kerangka kerja Django, yang biasanya digunakan untuk pengembangan web. Perbedaan utamanya adalah adanya Template yang bertanggung jawab untuk memproses tampilan, sementara dalam MVC, tampilan biasanya diolah oleh View.

3. **MVVM (Model-View-ViewModel):**
   - **Model:** Seperti dalam MVC dan MVT, Model mengurus data dan logika bisnis.
   - **View:** View adalah tampilan yang diberikan kepada pengguna, seperti dalam pola MVC dan MVT.
   - **ViewModel:** ViewModel adalah komponen yang menghubungkan Model dan View. Ini berisi logika tampilan dan berfungsi sebagai perantara antara Model dan View. ViewModel sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile dan aplikasi web kaya.

   **Perbedaan Utama:** MVVM adalah pola arsitektur yang lebih khusus digunakan dalam pengembangan antarmuka pengguna. ViewModel bertindak sebagai perantara antara Model dan View, memisahkan tampilan dan logika bisnis dengan baik. Ini sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang kompleks.

Saat memilih pola arsitektur untuk proyek Anda, penting untuk mempertimbangkan kebutuhan proyek dan jenis aplikasi yang Anda kembangkan. MVC dan MVT adalah pilihan umum untuk pengembangan web, sedangkan MVVM lebih umum digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna. Setiap pola memiliki kelebihan dan kelemahan sendiri, dan pilihan terbaik tergantung pada konteks proyek Anda.

