---
name: kotlin-android
description: >
  Skill completa para desenvolvimento Android moderno com Kotlin, Jetpack 
  Compose, Coroutines/Flow, arquitetura MVVM/Clean Architecture, injeção 
  de dependência (Hilt), testes, CI/CD, Material Design 3 e publicação 
  na Google Play Store.
alwaysApply: false
globs:
  - "**/*.kt"
  - "**/*.kts"
  - "**/build.gradle.kts"
  - "**/AndroidManifest.xml"
  - "**/compose/**"
triggerEvents:
  - "file:create:**/*.kt"
  - "command:review"
  - "command:android-generate"
---

# Kotlin Android — Skill de Desenvolvimento Mobile

## Stack e Versões

- **Kotlin 2.1+** (K2 compiler, multiplatform-ready)
- **Jetpack Compose BOM 2026+** (Material Design 3, Adaptive Layouts)
- **Gradle 8.x** com Kotlin DSL (`build.gradle.kts`)
- **Android SDK 35+** (compileSdk 35, minSdk 26, targetSdk 35)
- **Kotlin Coroutines + Flow** para assincronia
- **Hilt** (Dagger baseado) para DI
- **Room** para banco local
- **Retrofit + OkHttp + Kotlinx Serialization** para rede
- **Navigation Compose** para navegação
- **Compose Multiplatform** (opcional, para iOS + Android)

## Arquitetura MVVM + Clean Architecture

```
UI Layer (Compose) → ViewModel → UseCase → Repository → DataSource
      ↓                  ↓           ↓          ↓            ↓
   @Composable      StateFlow    Domain       Interface    Room/API
```

### Organização de Pacotes

```
com.meuapp/
├── di/               # Módulos Hilt
├── data/
│   ├── local/        # Room DAOs, entities
│   ├── remote/       # Retrofit services, DTOs
│   └── repository/   # Implementações de repositório
├── domain/
│   ├── model/        # Modelos de domínio (entidades puras)
│   ├── repository/   # Interfaces de repositório
│   └── usecase/      # Casos de uso
└── ui/
    ├── navigation/   # NavHost, rotas
    ├── screens/      # Telas (Compose + ViewModel por tela)
    ├── components/   # Componentes reutilizáveis
    └── theme/        # Theme, cores, tipografia MD3
```

### ViewModel + State

```kotlin
@HiltViewModel
class UsuarioListViewModel @Inject constructor(
    private val listarUsuariosUseCase: ListarUsuariosUseCase
) : ViewModel() {
    
    // UI State selado
    data class UiState(
        val usuarios: List<Usuario> = emptyList(),
        val isLoading: Boolean = false,
        val error: String? = null
    )
    
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    init {
        carregarUsuarios()
    }
    
    fun carregarUsuarios() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }
            listarUsuariosUseCase()
                .onSuccess { usuarios ->
                    _uiState.update { it.copy(usuarios = usuarios, isLoading = false) }
                }
                .onFailure { e ->
                    _uiState.update { it.copy(error = e.message, isLoading = false) }
                }
        }
    }
}
```

## Jetpack Compose + MD3

```kotlin
@Composable
fun UsuarioListScreen(
    viewModel: UsuarioListViewModel = hiltViewModel(),
    onUsuarioClick: (Long) -> Unit
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    Scaffold(topBar = { TopAppBar(title = { Text("Usuários") }) }) { padding ->
        Box(Modifier.padding(padding)) {
            when {
                uiState.isLoading -> CircularProgressIndicator(Modifier.align(Alignment.Center))
                uiState.error != null -> ErrorMessage(uiState.error!!)
                else -> LazyColumn {
                    items(uiState.usuarios, key = { it.id }) { usuario ->
                        UsuarioCard(usuario, onClick = { onUsuarioClick(usuario.id) })
                    }
                }
            }
        }
    }
}

@Composable
fun UsuarioCard(usuario: Usuario, onClick: () -> Unit, modifier: Modifier = Modifier) {
    Card(
        modifier = modifier.fillMaxWidth().clickable(onClick = onClick),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
        Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
            AsyncImage(model = usuario.avatarUrl, contentDescription = null,
                modifier = Modifier.size(48.dp).clip(CircleShape))
            Spacer(Modifier.width(12.dp))
            Column {
                Text(usuario.nome, style = MaterialTheme.typography.titleMedium)
                Text(usuario.email, style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        }
    }
}
```

## Coroutines + Flow (Assincronia)

### Regras

- **`viewModelScope.launch`** para chamadas do ViewModel
- **`lifecycleScope.launch`** para chamadas em Composables
- **`flowWithLifecycle()`** para coletar flows apenas no estado STARTED+
- **NUNCA** `GlobalScope`, `runBlocking`, ou `Thread.sleep()`
- **Tratamento**: `Result<T>`, `sealed class`, ou `Either` para erros

```kotlin
// No Composable — seguro para lifecycle
@Composable
fun <T> StateFlow<T>.collectAsStateWithLifecycle(): State<T> {
    val lifecycle = LocalLifecycleOwner.current.lifecycle
    return this.flowWithLifecycle(lifecycle, Lifecycle.State.STARTED)
        .collectAsState()
}
```

## Injeção de Dependência (Hilt)

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    
    @Provides
    @Singleton
    fun provideAppDatabase(@ApplicationContext context: Context): AppDatabase {
        return Room.databaseBuilder(
            context, AppDatabase::class.java, "meuapp.db"
        ).build()
    }
    
    @Provides
    fun provideUsuarioDao(db: AppDatabase): UsuarioDao = db.usuarioDao()
}
```

## Persistência (Room)

```kotlin
@Entity(tableName = "usuarios")
data class UsuarioEntity(
    @PrimaryKey val id: Long,
    val nome: String,
    val email: String,
    val avatarUrl: String?,
    val ultimaSincronizacao: Long = System.currentTimeMillis()
)

@Dao
interface UsuarioDao {
    @Query("SELECT * FROM usuarios ORDER BY nome ASC")
    fun listarTodos(): Flow<List<UsuarioEntity>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun inserirTodos(usuarios: List<UsuarioEntity>)
    
    @Query("DELETE FROM usuarios")
    suspend fun limpar()
}
```

## Networking (Retrofit + Kotlinx Serialization)

```kotlin
@Serializable
data class UsuarioDto(
    val id: Long,
    @SerialName("first_name") val firstName: String,
    @SerialName("last_name") val lastName: String,
    val email: String,
    val avatar: String?
)

interface UsuarioApi {
    @GET("users")
    suspend fun listar(): List<UsuarioDto>
    
    @GET("users/{id}")
    suspend fun buscarPorId(@Path("id") id: Long): UsuarioDto
}
```

## Navigation Compose

```kotlin
@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    
    NavHost(navController, startDestination = "usuarios") {
        composable("usuarios") {
            UsuarioListScreen(onUsuarioClick = { id ->
                navController.navigate("usuarios/$id")
            })
        }
        composable(
            route = "usuarios/{id}",
            arguments = listOf(navArgument("id") { type = NavType.LongType })
        ) { backStackEntry ->
            val id = backStackEntry.arguments?.getLong("id") ?: return@composable
            UsuarioDetalheScreen(usuarioId = id)
        }
    }
}
```

## Testes

```kotlin
// Unit test — ViewModel + UseCase mockado
@OptIn(ExperimentalCoroutinesApi::class)
class UsuarioListViewModelTest {
    
    @get:Rule
    val rule = MainCoroutineRule()
    
    @Test
    fun `carregarUsuarios quando sucesso atualiza lista`() = runTest {
        val mockUseCase = mockk<ListarUsuariosUseCase>()
        every { mockUseCase() } returns Result.success(listaMock)
        
        val vm = UsuarioListViewModel(mockUseCase)
        vm.carregarUsuarios()
        
        val state = vm.uiState.first { !it.isLoading }
        assertEquals(listaMock, state.usuarios)
        assertNull(state.error)
    }
    
    @Test
    fun `carregarUsuarios quando erro mostra mensagem`() = runTest {
        val mockUseCase = mockk<ListarUsuariosUseCase>()
        every { mockUseCase() } returns Result.failure(IOException("sem rede"))
        
        val vm = UsuarioListViewModel(mockUseCase)
        vm.carregarUsuarios()
        
        val state = vm.uiState.first { !it.isLoading }
        assertTrue(state.usuarios.isEmpty())
        assertEquals("sem rede", state.error)
    }
}

// Compose UI test
@Test
fun usuarioCard_exibeNome() {
    composeTestRule.setContent {
        MaterialTheme {
            UsuarioCard(usuario = usuarioMock, onClick = {})
        }
    }
    composeTestRule.onNodeWithText("João Silva").assertIsDisplayed()
}
```

## Build & CI/CD

```kotlin
// build.gradle.kts (project) — Kotlin 2.1 + Compose compiler plugin
plugins {
    id("com.android.application") version "8.7.0" apply false
    id("org.jetbrains.kotlin.android") version "2.1.0" apply false
    id("org.jetbrains.kotlin.plugin.compose") version "2.1.0" apply false
    id("com.google.dagger.hilt.android") version "2.51" apply false
    id("com.google.devtools.ksp") version "2.1.0-1.0.29" apply false
}
```

- **Gradle Enterprise** para cache de build
- **Dependabot** para atualizações automáticas
- **GitHub Actions**: lint → unit test → instrumented test → build APK
- **Play Store**: Upload via `publish` task + Play Console API
- **ProGuard/R8**: Mapping file versionado, obfuscation desligado em debug

## Performance

- **LazyColumn**: `key` obrigatório, evitar recomposição com `remember`
- **Imagens**: Coil ou Glide com cache de disco, placeholders
- **State**: `collectAsStateWithLifecycle()` sobre `collectAsState()`
- **DerivedStateOf**: Para estados computados (não em `remember` com cálculo)
- **Tracing**: `AsyncTrace.beginSection()` para telas lentas
- **Baseline profiles**: Gerar com Macrobenchmark para startup instantâneo

## Boas Práticas Kotlin

- **NUNCA** usar `!!` (!! assertions) em produção — usar `?:`, `?.`, ou `.requireNotNull()`
- **NUNCA** `GlobalScope` — escopos têm lifecycle
- **NUNCA** `Data Class` para entidades de domínio (preferir classe selada ou data class com validação)
- **Usar** `sealed class` para estados de UI
- **Usar** `inline value classes` para IDs tipados: `@JvmInline value class UsuarioId(val value: Long)`
- **Usar** `context receivers` para dependências em funções (Kotlin 2.1+)
- **Usar** `immutable collections` (`listOf`, `mapOf`) por padrão

## Gatilhos de Uso

- **Criar tela**: Compose + ViewModel + StateFlow + Hilt
- **Criar API call**: Retrofit service + DTO + Repository + UseCase
- **Criar banco**: Room Entity + DAO + Database class + Migration
- **Navegação**: Navigation Compose + argumentos + deep links
- **Revisar PR**: Recomposição excessiva, memory leaks, coroutines soltas, nullable sem tratamento
- **Publicar**: Build release + ProGuard + Play Console + Versionamento semântico

## Provedores de Referência

- Android Developers: https://developer.android.com/docs
- Kotlin Docs: https://kotlinlang.org/docs/home.html
- Jetpack Compose Docs: https://developer.android.com/compose
- Material Design 3: https://m3.material.io/
- Hilt Guide: https://dagger.dev/hilt/
