<template>
    <div class="block relative w-screen lg:w-full bg-contain home-block">
        <div class="flex container top-10 justify-center relative flex-wrap bg-opacity-75">
            <div class="absolute top-[7rem]">
                <div class="text-slate-800 z-50">
                    <h1 class="md:text-6xl text-5xl font-mono font-semibold">
                        Pezeshkino
                    </h1>
                </div>
            </div>
            <div class="z-50 absolute top-[12.8em]">
                <div class="flex flex-nowrap flex-row border shadow-lg shadow-slate-600/20 border-slate-800 rounded-lg md:scale-100 scale-90">
                    <button 
                            class="bg-slate-800 flex items-center justify-center gap-2 text-white hover:bg-slate-700 py-2 px-3 sm:py-4 sm:px-7 search-button" 
                            @click="searchAll"
                           >
                        <i class="fas fa-search text-xl"></i>
                        جستجو
                    </button>
                    <select 
                            class="lg:px-7 w-24 lg:w-[12rem] px-1.5 ms:px-1 md:px-3 hover:bg-slate-200 hover:cursor-pointer"
                            @change="selectProvince"
                            v-model="province"
                            name="province"
                           >
                        <option class="text-right" value="">استان</option>
                        <option 
                                v-for="ostan in getProvinces" 
                                :key="ostan" 
                                class="text-right"
                               >
                            {{ ostan }}
                        </option>
                    </select>
                    <select 
                            id="shahrSelect" 
                            class="lg:px-7 w-24 lg:w-[12rem] text-right px-1.5 ms:px-1 md:px-3 hover:bg-slate-200 hover:cursor-pointer"
                            v-model="city"
                            name="city"
                           >
                        <option value="">شهر</option>
                    </select>
                    <input 
                           class="lg:px-7 w-28 lg:w-[16.5rem] px-1.5 ms:px-1 md:px-3 text-right rounded-lg search-text" 
                           type="text" 
                           style="direction: rtl;"
                           placeholder="نام پزشک، تخصص..."
                           name="searchText"
                           v-model="searchText"
                          >
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="block relative top-[26rem] bg-black w-full py-12 px-10">
                <div class="grid grid-cols-2 gap-8 text-white">
                    <div>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit, illum libero, quod, atque itaque numquam voluptates inventore sapiente explicabo ex culpa odit provident hic nulla laboriosam quidem alias repellendus nisi optio nemo quibusdam. Qui, optio sed! Culpa eligendi, sequi, debitis dolore ab possimus odit dolores delectus explicabo cupiditate magnam! Culpa odit suscipit minima provident numquam ea dolor saepe, sapiente magnam veritatis reiciendis ex a officiis dolores sit impedit ipsum unde quia sequi quidem commodi iure optio voluptate. Odit, aut dolores eveniet fugit debitis animi dignissimos? Laboriosam, dolore nisi labore veritatis ab a? Atque assumenda quasi quam rerum quis nobis, culpa architecto fugiat exercitationem aperiam sapiente magnam saepe officiis reiciendis? Assumenda saepe culpa nesciunt odit magnam quibusdam deleniti hic voluptatum harum dicta maiores corrupti eveniet, sed, inventore error laborum itaque nisi facere? Dolorem, inventore vitae. Aperiam obcaecati voluptate nam commodi eaque accusamus ab exercitationem repellendus quam rem a fugit beatae dolorem, nesciunt asperiores alias sed laboriosam, soluta in. Quos tempore magnam quam sed dolore commodi ab ipsum sunt. Temporibus, accusantium. Magnam numquam accusantium modi dolores. Laudantium laborum repellendus maiores aperiam repudiandae voluptate, et esse voluptas aliquid numquam alias eveniet quaerat. Explicabo iusto et molestiae eaque quod perferendis, placeat earum doloremque deleniti rerum vitae veniam! Doloremque accusamus obcaecati veniam, ex corrupti commodi quae totam molestiae? Recusandae minima soluta reiciendis mollitia laboriosam sit in ipsum eligendi deleniti voluptatum laudantium enim officia sapiente distinctio excepturi repellat, veritatis, neque debitis ratione nihil voluptatem necessitatibus? Animi nobis, ducimus quod tenetur pariatur maxime quaerat saepe, aperiam quia, consequuntur autem molestiae! Neque optio magni aperiam quia! Non nostrum perferendis iste. Minima neque vero explicabo praesentium incidunt exercitationem esse ratione quia officiis qui, quos deleniti? Nobis vitae temporibus iure voluptate hic atque, tenetur delectus. Nobis deserunt at rerum harum incidunt atque molestiae. Veritatis tempora modi obcaecati atque eveniet fuga doloremque ab reiciendis veniam dolore eius corporis, reprehenderit distinctio exercitationem earum perspiciatis recusandae ipsa sunt dolorem nisi vero minima labore. Repellat recusandae corrupti eligendi, ut laboriosam totam ipsam unde inventore blanditiis accusamus, consequatur perspiciatis aliquam eveniet quod nam suscipit voluptatum expedita dolores est alias. Possimus obcaecati corrupti laudantium. Omnis quibusdam similique quasi! Pariatur aliquam delectus debitis eveniet rerum tempore autem nulla a reprehenderit nisi cumque deleniti, hic, earum facere ea rem molestiae amet? Necessitatibus nesciunt quas tempora delectus corrupti nihil tempore facere deleniti! Excepturi maxime officiis debitis, quisquam doloremque temporibus iusto nam repudiandae unde animi itaque. Fuga eum fugiat alias a assumenda, aliquid ipsam cupiditate illo. Totam unde quasi quidem voluptatum maiores distinctio inventore perferendis quos magnam minus quaerat deserunt nam pariatur, in at aperiam, eius quam voluptas quae dolore? Obcaecati, ipsam laudantium illo est illum eaque molestias reprehenderit eligendi doloremque debitis excepturi libero minima nesciunt reiciendis? Odit ipsam ratione repudiandae odio dolor cupiditate nihil tenetur, voluptatum, dolore eos numquam. Dolore vel iusto sunt commodi nulla libero beatae pariatur sapiente ab dignissimos suscipit, repudiandae placeat! Quisquam ex veniam beatae repellendus similique sequi eaque ratione quae ea vitae, asperiores voluptates harum ab ducimus natus omnis repudiandae porro consequatur! Excepturi, ducimus expedita.
                        </p>
                    </div>
                    <div>
                        <p>
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Vero sint ad amet earum tempora aut. Laborum accusantium quis corrupti, vero voluptatibus amet laboriosam impedit laudantium perferendis unde odit facere odio voluptates iusto sequi eligendi id quaerat? Repellendus est, consectetur perferendis, quis laboriosam odio ducimus excepturi vitae explicabo asperiores amet voluptatem inventore non obcaecati ipsam quasi? Numquam voluptates quibusdam rerum eius laudantium voluptate fuga quo assumenda accusantium soluta earum alias quae, libero, blanditiis hic voluptatibus vero et beatae quasi aspernatur accusamus nisi modi? Deserunt nihil earum blanditiis odit natus non, magni consectetur ad sequi illo dolor corrupti quis doloribus quas enim possimus obcaecati? Quos quam ea repudiandae fugit omnis. Explicabo eveniet laudantium minima magni architecto non voluptatibus voluptas cupiditate maiores! Deleniti laborum quod, facilis aliquid eveniet dolorum eum tempora autem saepe quisquam pariatur? Ipsa non inventore accusantium praesentium, repudiandae voluptatem laudantium veritatis fugit, commodi voluptatum dolores. Placeat earum fugit mollitia reiciendis voluptatibus vero magni, dignissimos laboriosam vel? Illum autem dignissimos libero laboriosam, distinctio est nobis quos labore possimus suscipit molestias ab accusamus sit similique esse saepe quidem voluptatibus impedit! Dolorem eos nulla voluptatibus quia officiis temporibus iusto sequi libero quasi obcaecati aliquam ab culpa similique ut sint quibusdam delectus sed iure, vero quis magnam! Nemo dolorum tenetur placeat nulla quibusdam quo temporibus! Nemo fuga rerum saepe praesentium ut assumenda hic quidem magni architecto, maxime placeat minima minus nulla, repellat vero tenetur asperiores, a atque aperiam fugit vel ea reprehenderit. Perspiciatis, quod labore impedit ducimus sint fugit voluptates sapiente aut? Eaque quisquam maiores aut porro sapiente quae, tempore id consequatur quaerat. Cum repellat quo commodi sed molestias eum placeat fuga asperiores totam? Sequi aspernatur dolor impedit quas earum adipisci laboriosam architecto sint, velit neque quo perspiciatis debitis in ab eos repellendus aliquid similique deleniti blanditiis itaque nesciunt tenetur atque accusantium molestias! Enim similique ipsa iste, tempora maiores repellat rerum quibusdam. Non tempora debitis ipsam numquam itaque mollitia, tenetur at ipsa sunt, repellendus nobis odio sint hic praesentium similique consectetur voluptate! Suscipit at, amet nemo voluptates delectus eligendi. Optio maxime quo nihil magni ipsum dolorem nesciunt recusandae at repudiandae. Est non aperiam nemo libero soluta nostrum eos necessitatibus, nobis suscipit nesciunt consequatur aut maxime, reiciendis assumenda quo, nam accusantium modi. Quibusdam adipisci non enim fuga deserunt aliquam, quam unde perspiciatis nisi voluptatibus distinctio voluptas totam culpa ad, a quo veniam aperiam quod laudantium facere facilis modi, consequatur deleniti velit. Possimus, maiores quisquam dolorem praesentium magni iure deleniti amet debitis ut impedit, at dolores tempora eius nostrum nemo deserunt, doloremque maxime cumque eaque nihil? Praesentium placeat delectus nesciunt molestiae. Quibusdam rem at ducimus. Nemo ab beatae eaque sed tenetur itaque, adipisci eos eligendi dicta placeat nulla recusandae! Odit atque minima voluptates minus iure officia? Repudiandae quis laboriosam quia quisquam ea animi, hic est nam non nemo maxime dignissimos asperiores necessitatibus corrupti cumque minima pariatur cum ex expedita aut ratione? Recusandae, totam porro ratione debitis velit iure rem cumque laudantium excepturi iste veniam temporibus ad facilis fugiat voluptates rerum nobis id repudiandae nulla cum aperiam similique. Dolorem, rem excepturi, repellendus quia ipsum nostrum similique est ad corporis, nesciunt mollitia voluptas. Dolore corporis accusamus quidem, possimus labore vel obcaecati! Quasi cupiditate ratione nulla tempora recusandae error, dolor est corrupti impedit expedita iusto eaque repudiandae vitae tenetur et saepe consequuntur voluptate veritatis, reprehenderit ab? Natus aspernatur quaerat, animi corporis saepe iure id dignissimos facere ducimus eos doloremque ea debitis ipsam officiis cum iusto totam soluta dolore ipsum quasi hic pariatur laborum sed. Ad consectetur vero aliquid. Aperiam doloremque tempore non ea! A necessitatibus quaerat dolor quo, ipsam magni culpa excepturi debitis suscipit nihil ipsum blanditiis cupiditate consequatur doloribus illo perspiciatis tenetur, minima laborum architecto porro enim, odit dolorem ducimus quis. Ab sit omnis numquam corporis. Error quas magni officia et, ea consequatur quidem deserunt tempora tempore saepe illum. Molestiae quos laudantium recusandae voluptas? Corporis nihil impedit omnis dicta ratione aspernatur tenetur cum voluptate illo esse beatae earum fugit, eveniet laborum officiis saepe qui amet id natus inventore velit? Corrupti nisi, quibusdam libero reprehenderit vel veritatis adipisci laudantium inventore laboriosam praesentium ducimus quas, earum fugiat sit molestias, dolor necessitatibus repellendus sint ex omnis voluptas ipsum molestiae! Amet animi distinctio modi, optio beatae architecto assumenda? Quibusdam tempore quia doloribus nostrum, architecto quo facere reprehenderit atque tenetur hic voluptas facilis obcaecati sunt ipsum, necessitatibus natus nisi corrupti illo eum, odio repellat! Eaque, tempora deleniti. Quibusdam, maxime error eos ut iure enim corporis, illum tempora velit est sint unde perferendis nam exercitationem eum rerum, recusandae dolores. Animi earum, quo accusantium saepe maxime reiciendis, ipsa explicabo placeat perferendis nesciunt id! Deserunt fugiat, iure, labore veniam fuga quod reiciendis earum ducimus vel amet nobis sed doloremque ab, dolore dicta beatae ex neque natus culpa quasi aliquam ut repellendus. Id cumque nulla iste odit aut fugit quibusdam esse maiores! Fugiat, possimus culpa velit omnis eligendi repellat, obcaecati reprehenderit vel, ipsam minus nisi amet. Perferendis, quo? Ipsa quas aliquid deserunt dicta in veritatis accusamus pariatur velit nihil assumenda illum beatae provident consectetur, corporis soluta doloremque iusto error quia officia id. Optio necessitatibus dignissimos atque voluptate soluta vero labore doloremque deleniti perspiciatis, cupiditate debitis incidunt ratione unde tenetur, quibusdam expedita vitae aliquid quisquam ut laborum dicta! Error ullam nam velit consectetur rerum architecto tenetur et, repellat autem ipsam iure aliquam ducimus provident, ipsa eos ex! Quas temporibus praesentium molestias sit distinctio soluta harum ducimus in aliquid iure cum quasi, id perferendis cumque dolore impedit molestiae officiis ipsa, recusandae quae? Magnam tempore sint quos quis officia minus natus fugit? Accusantium facere, perspiciatis porro, laudantium magnam minus suscipit amet saepe dolor non aliquam possimus sunt inventore, quaerat tempore eligendi? Reiciendis, odio earum. Corporis fuga ratione ducimus architecto nam eum tenetur aperiam consequuntur repellat, animi vitae minima, officiis pariatur molestias praesentium quisquam ipsa temporibus vel? Quisquam cum quidem in, distinctio animi similique assumenda placeat expedita. Quas accusamus aut vero esse neque fugiat, quis, suscipit sit laudantium tempora vel tempore nihil ratione eligendi laboriosam animi consequatur architecto illo, ea accusantium! Dolore sed, sint cupiditate suscipit ad optio a provident sit.
                        </p>
                    </div>
                </div>
            </div>
            <HomeFooter />
        </div>
    </div>
</template>

<style scoped>
    .home-block {
        background-image: url(@/assets/bg-home.webp);
    }
    .search-button {
        border-radius: .25rem 0 0 .25rem;
    }
    .search-text {
        border-radius: 0 .45rem .45rem 0;
    }
</style>

<script>
    import { mapState, mapGetters } from 'vuex'
    import HomeFooter from '@/components/HomeFooter.vue'

    export default {
        name: 'HomeSection',
        data() {
            return {
                province: "",
                city: "",
                searchText: ""
            }
        },
        components: {
            HomeFooter
        },
        computed: {
            ...mapState(["locations"]),
            ...mapGetters({getProvinces: "locations/getProvinces"})
        },
        methods: {
            scrollToTop() {
                scrollTo(0, 0)
            },
            updateLocation() {
                if (this.locations.provinces_cities.length === 0) {
                    this.$store.dispatch("locations/fetchLocation")
                }
            },
            selectProvince(e) {
                const cities = this.locations.provinces_cities.find(v => v.name == e.target.value).cities
                const selectElement = document.getElementById("shahrSelect")
                selectElement.innerHTML = ""
                let node;
                for (let i = 0 ; i < cities.length ; i++) {
                    node = document.createElement("option")
                    node.text = cities[i].name
                    node.value = cities[i].id
                    selectElement.appendChild(node)
                }
            },
            searchAll() {
                this.$router.push({
                    path: 'doctors',
                    query: {
                        search: this.$data.searchText
                    }
                })
            }
        },
        mounted() {
            if (this.locations.provinces_cities.length === 0) {
                this.$store.dispatch("locations/fetchLocation")
            }
        }
    }
</script>