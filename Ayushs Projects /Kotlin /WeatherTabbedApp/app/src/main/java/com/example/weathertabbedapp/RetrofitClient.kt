package com.example.weathertabbedapp

object RetrofitClient {
    object RetrofitClient {
        private const val BASE_URL = "http://dataservice.accuweather.com/"

        val instance: ApiService by lazy {
            val retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()

            retrofit.create(ApiService::class.java)
        }
    }

}