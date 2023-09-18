Naufal Ichsan - 2206082013 - F  
**PBP Tugas 2**    
**Step by Step**
1. **Membuat sebuah proyek Django baru.**  
      1. Membuat direktori baru bernama weapon_inventory.  
      2. Menginisiasi virtual environment yang saya beri nama env dan mengaktifkannya dengan command 'source env/bin/ activate'      
      3. Melakukan download seluruh dependencies termasuk django itu sendiri melalui requirements.txt menggunakan pip didalam virtual environment     
      4. Menggunakan command 'django-admin startproject weapon_inventory .' untuk menginisasi project django baru bernama weapon_inventory      
2. **Membuat aplikasi dengan nama main pada proyek tersebut.**     
      1. Menggunakan command 'python3 manage.py startapp weapons --> saya memberi nama app saya weapons bukan main,    
      menurut saya nama ini lebih cocok untuk membuat sebuah weapon inventory      
      2. Saya mendaftarkan app weapons kedalam settings --> INSTALLED APPS yang ada pada projek weapon_inventory     
3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**     
      1. Saya membuat file urls.py pada app weapon terlebih dahulu       
      2. Saya mengimpor include pada urls.py pada proyek untuk memasukkan urls pada aplikasi weapons pada list urlpattern Syntax saya gunakan adalah 'path('', include('weapons.urls'))' --> pada syntax terdapat 'path('', url) disini saya   beri string kosong agar app langsung keredirect ke weapons.views ketika link diklik   
4. **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.**   
   - **name sebagai nama item dengan tipe CharField.**   
   - **amount sebagai jumlah item dengan tipe IntegerField.**   
   - **description sebagai deskripsi item dengan tipe TextField.**   
      1. Saya melakukan import models dari djangodb   
      2. Saya membuat class Weapon yang isinya adalah atribut seperti diatas   
      3. Saya menambahkan beberapa attributes seperti atk, critrate, dan critdmg yang menurut saya relevan dengan weapons attributes      
5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**    
      1. Saya membuat folder templates terlebih dahulu yang isinya merupakan template html yang saya beri nama weapons.html untuk menampilkan apa yang ada di views    
      2. Saya melakukan import render dari django.shortcut pada views.py dan membuat function show_weapons yang berfungsi menampilkan weapons weapons yang ada    
      3. Di dalam Function saya membuat suatu dict yang berisi key berdasarkan models yang sudah dibuat dan valuenya.   
      4. Setelahnya, saya melakukan return kepada weapons.html agar data yang ada di views dapat ditampilkan oleh html   
6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**   
      1. saya membuat berkas urls.py pada direktori weapons yang nantinya akan disi urlpatterns juga, nantinya urlpatterns ini akan diarahkan ke fungsi show_weapons yang ada pada weapons.views   
7.  **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**   
      1. Melakukan deploy ke adaptable seperti pada tutorial 0 yang membedakan adalah pada start command diberikan perintah 'python manage.py migrate && gunicorn weapon_inventory.wsgi' agar mengarah ke wsgi weapon_inventory   

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**        

   Request----------------urls.py------------------------views.py-------------models.py-------------Templates   
   ---↓-----------------------↓------------------------------↓---------------------↓----------------------↓     
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



**PBP Tugas 3**    
**Apa perbedaan antara form POST dan form GET dalam Django?**  
Pada Django, baik metode POST maupun GET adalah metode HTTP yang digunakan untuk mengirim data dari browser ke server. Namun, keduanya memiliki perbedaan utama dalam cara mereka mengirim dan mengelola data:

1. **Metode POST**:

   - **Keamanan**: Metode POST lebih aman dibandingkan dengan GET karena data yang dikirim melalui metode POST tidak terlihat di URL. Data dikirim sebagai "request body" dan tidak terlihat oleh pengguna atau di history browser.
   
   - **Penggunaan**: Metode POST digunakan ketika Anda ingin mengirim data yang sensitif atau data yang akan mengubah keadaan server, seperti mengirim data formulir yang akan menyimpan atau memperbarui data di database.

   - **Pemrosesan**: Data yang dikirim dengan metode POST dapat diakses di Django menggunakan `request.POST` dalam view Anda. Data ini biasanya digunakan untuk memproses formulir, menyimpan data, atau melakukan tindakan lain yang mengubah server.

   - **Pembatasan Panjang Data**: Metode POST tidak memiliki batasan panjang data yang diterima, sehingga Anda dapat mengirim data yang lebih besar daripada metode GET.


2. **Metode GET**:

   - **Visibilitas**: Data yang dikirim dengan metode GET ditambahkan ke URL, yang berarti data ini terlihat di bilah alamat browser. Ini tidak aman untuk data sensitif karena dapat dengan mudah dilihat oleh pengguna atau terekam dalam history browser.

   - **Penggunaan**: Metode GET digunakan ketika Anda ingin mengambil data dari server tanpa mengubah keadaan server. Ini adalah metode yang umum digunakan untuk mengambil halaman web, pencarian, atau berbagi tautan.

   - **Pemrosesan**: Data yang dikirim dengan metode GET dapat diakses di Django menggunakan `request.GET` dalam view Anda. Data ini biasanya digunakan untuk mengambil parameter atau query string dari URL.

   - **Pembatasan Panjang Data**: Metode GET memiliki batasan panjang data yang dapat dikirim melalui URL. Ini tergantung pada pengaturan server web dan browser, dan data yang terlalu panjang dapat terpotong.

**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**   
XML, JSON, dan HTML adalah tiga format yang umum digunakan untuk mengirim dan menyimpan data dalam konteks pengembangan perangkat lunak web dan aplikasi. Berikut adalah perbedaan utama antara ketiganya:

1. **XML (Extensible Markup Language)**:

   - **Struktur**: XML adalah bahasa markup yang digunakan untuk mengatur dan mengstruktur data. Ia memiliki sintaks yang ketat dengan tag pembuka dan penutup, yang dapat membungkus data dan atribut.

   - **Tujuan Utama**: XML sering digunakan untuk pertukaran data antara aplikasi yang berbeda atau untuk menyimpan data dalam format yang dapat diolah secara struktural.

   - **Fleksibilitas**: XML sangat fleksibel dan memungkinkan Anda mendefinisikan struktur data Anda sendiri menggunakan Dokumen DTD (Document Type Definition) atau XML Schema.

   - **Ekstensibilitas**: XML dapat digunakan untuk mendefinisikan bahasa markup yang khusus untuk aplikasi tertentu.

   - **Contoh**: 
     ```xml
     <person>
         <name>John Doe</name>
         <age>30</age>
     </person>
     ```

2. **JSON (JavaScript Object Notation)**:

   - **Struktur**: JSON adalah format yang terdiri dari pasangan nama-nilai (key-value pairs). Ia lebih ringkas dibandingkan dengan XML karena tidak memiliki tag pembuka dan penutup.

   - **Tujuan Utama**: JSON digunakan untuk pertukaran data antara klien dan server web dalam aplikasi web dan API RESTful. JSON juga digunakan secara luas dalam penyimpanan data dan konfigurasi.

   - **Fleksibilitas**: JSON memiliki struktur yang lebih sederhana dibandingkan XML dan biasanya lebih mudah dibaca oleh manusia.

   - **Ekstensibilitas**: JSON lebih terbatas dalam hal definisi struktur data dibandingkan dengan XML.

   - **Contoh**: 
     ```json
     {
         "name": "John Doe",
         "age": 30
     }
     ```

3. **HTML (Hypertext Markup Language)**:

   - **Struktur**: HTML adalah bahasa markup yang digunakan untuk membuat halaman web dan mengatur tampilan konten web. Ia memiliki elemen-elemen yang mendefinisikan struktur dan tampilan halaman web.

   - **Tujuan Utama**: HTML digunakan untuk membuat halaman web yang dapat diakses oleh browser. Ia tidak digunakan secara langsung untuk pertukaran data antara aplikasi, meskipun bisa digunakan untuk menampilkan data dalam bentuk yang dapat dilihat oleh pengguna.

   - **Fleksibilitas**: HTML memiliki struktur yang terbatas dan terkait erat dengan tampilan halaman web.

   - **Ekstensibilitas**: HTML memiliki elemen-elemen bawaan yang didefinisikan oleh spesifikasi HTML dan tidak dapat diperluas dengan mudah seperti XML.

   - **Contoh**: 
     ```html
     <html>
         <head>
             <title>Contoh Halaman HTML</title>
         </head>
         <body>
             <h1>Selamat datang!</h1>
             <p>Ini adalah contoh halaman HTML.</p>
         </body>
     </html>
     ```

Dalam konteks pengiriman data, XML dan JSON lebih sering digunakan untuk mengirim data antara aplikasi, sementara HTML digunakan untuk membuat halaman web yang dapat dilihat oleh pengguna melalui browser. Pemilihan format tergantung pada kebutuhan aplikasi dan tipe data yang akan ditangani.  

**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**  
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan yang membuatnya sangat cocok untuk tugas ini:

1. **Ringkas dan Mudah Dibaca**: JSON memiliki struktur yang sederhana dengan pasangan nama-nilai (key-value pairs) yang membuatnya mudah dibaca dan ditulis oleh manusia. Ini membuatnya sangat berguna untuk debugging dan pengembangan.

2. **Penggunaan dalam JavaScript**: JSON berasal dari JavaScript, sehingga sangat mudah diintegrasikan dengan kode JavaScript yang banyak digunakan dalam pengembangan web. Ini memungkinkan data JSON untuk digunakan langsung dalam JavaScript tanpa perlu parsing yang rumit.

3. **Kemampuan Parsing**: Sebagian besar bahasa pemrograman memiliki dukungan bawaan atau pustaka untuk parsing JSON. Ini membuatnya sangat mudah diimplementasikan dalam aplikasi yang ditulis dalam berbagai bahasa pemrograman.

4. **Ringan**: JSON adalah format yang ringan, artinya tidak ada tambahan berat data seperti tag pembuka dan penutup seperti pada XML. Ini mengurangi overhead dalam pertukaran data.

5. **Bacaan dan Penulisan Data**: JSON mendukung berbagai tipe data, termasuk string, angka, boolean, array, dan objek. Ini membuatnya sangat fleksibel dalam menggambarkan data dari berbagai jenis.

6. **Kompatibilitas Web**: JSON sangat kompatibel dengan web dan digunakan secara luas dalam pengembangan aplikasi web, terutama dalam API RESTful. Banyak layanan web, seperti API media sosial dan layanan cloud, menyediakan data dalam format JSON.

7. **Parsial dan Penanganan Kesalahan**: JSON memungkinkan untuk memetakan bagian tertentu dari objek atau array, yang berguna ketika Anda hanya perlu mengambil sebagian dari data yang tersedia. Selain itu, JSON dapat dengan mudah menangani kesalahan tanpa menghentikan pengolahan keseluruhan dokumen.

8. **Desentralisasi**: JSON tidak memerlukan skema sentral yang ketat seperti XML. Ini memungkinkan aplikasi mengirim data tanpa harus mengikuti skema yang sudah ditentukan sebelumnya.

9. **Dukungan Cross-platform**: JSON dapat digunakan untuk pertukaran data antara berbagai platform, termasuk aplikasi web, aplikasi seluler, dan layanan server.

Dengan semua keunggulan ini, JSON telah menjadi format pertukaran data yang sangat populer dalam pengembangan aplikasi web modern, terutama dalam konteks RESTful API, di mana ia memungkinkan komunikasi yang efisien dan mudah diimplementasikan antara klien dan server.  

**Step by Step**  
1. **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
   1.  Sebelum membuat form saya membuat templates di root folder dan mengisinya dengan skeleton `base.html` dan menambahkannya ke TEMPLATES pada `settings.py` untuk menerapkannya sebagai kerangka yang ada pada templates pada folder weapons.
   2. setelah itu saya membuat `forms.py` pada folder weapons, tujuannya adalah untuk menambahkan input data dari user.
   3. Saya membuat class WeaponForm yang memiliki model yang diambil dari class Weapon dan memiliki fields sesuai dengan atribut yang dimiliki class Weapon dari `models.py`.
   4. Setelahnya saya membuat `add_weapons.html` pada templates yang ada pada folder weapons menggunakan format yang ada pada `base.html`, tidak lupa untuk mengganti format untuk `weapons.html` juga.

2. **Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**  
   1. Hal yang pertama saya lakukan adalah melakukan import HttpResponse dari django.http dan reverse dari django.urls pada `views.py`
   2. Lalu saya membuat fungsi add_weapons yang bertujuan untuk menampilkan data dalam format HTML
   3. Saya juga menambahkan fungsi show_xml, show_json, show_xml_by_id, show_json_by_id seperti pada tutorial untuk menampilkan data dalam bentuk xml dan json dan mencari data berdasarkan idnya nantinya fungsi ini akan melakukan return HttpResponse dengan serializer yang berfungsi untuk mengubah data menjadi format yang diinginkan.
   4. Tidak lupa pada fungsi show_weapons saya menambahkan variable `weapons = Weapon.objects.all()` yang bertujuan untuk melakukan return pada setiap objek dari class Weapon yang sudah dibuat. variable weapons ini juga dimasukkan kedalam context untuk dipanggil dalam html nantinya.
   
3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
 1. Menambahkan url pattern pada `urls.py` yang ada pada folder weapons. 
 berikut url untuk masing masing function yang telah dibuat pada `views.py`
 ```python
 ...
path('add_weapons', add_weapons, name='add_weapons'),
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
...
 ```
   

   








**Screenshot Pengaksesan Data**   
- **XML**  
![Alt text](Screenshot/xml.png)
- **XML/Id**
![Alt text](Screenshot/xml-id.png)  
- **JSON** 
![Alt text](Screenshot/json.png) 
- **JSON/Id**
![Alt text](Screenshot/json-id.png)  
- **HTML**
![Alt text](Screenshot/html.png)