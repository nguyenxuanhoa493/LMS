import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.role import add_role_to_course

list_course = [
    {"iid": 56988202, "name": "Sinh học lớp 7B", "id": "6589c5e3f3561b894700385d"},
    {"iid": 56988203, "name": "Lịch sử lớp 7B", "id": "6589c5e3cd8500cf1e031621"},
    {"iid": 56988204, "name": "Địa lí lớp 7B", "id": "6589c5e3ba2d672bc60698bb"},
    {"iid": 56988201, "name": "Vật lí lớp 7B", "id": "6589c5e3b4f7cd02e40cd40f"},
    {
        "iid": 56988196,
        "name": "Giáo dục thể chất lớp 7B",
        "id": "6589c5e2c9a599a1b20061c8",
    },
    {
        "iid": 56988198,
        "name": "Hoạt động trải nghiệm lớp 7B",
        "id": "6589c5e232b7d19b990b7209",
    },
    {"iid": 56988197, "name": "Tiếng anh lớp 7B", "id": "6589c5e21adead3cad0fe2fc"},
    {"iid": 56988200, "name": "Công nghệ lớp 7B", "id": "6589c5e213fe629005058513"},
    {
        "iid": 56988199,
        "name": "Giáo dục công dân lớp 7B",
        "id": "6589c5e2129b054fba013428",
    },
    {"iid": 56988195, "name": "Mĩ thuật lớp 7B", "id": "6589c5e194ef9b71930b9abd"},
    {"iid": 56988192, "name": "Toán lớp 7B", "id": "6589c5e13410e4085d04faa2"},
    {"iid": 56988193, "name": "Ngữ văn lớp 7B", "id": "6589c5e125c56a7861063bea"},
    {"iid": 56988194, "name": "Âm nhạc lớp 7B", "id": "6589c5e11b4443a43404a580"},
    {"iid": 56988187, "name": "Công nghệ lớp 7C", "id": "6589c5e0f5c14222ec0a78ec"},
    {"iid": 56988189, "name": "Sinh học lớp 7C", "id": "6589c5e0b3f80c63d2071c4f"},
    {"iid": 56988188, "name": "Vật lí lớp 7C", "id": "6589c5e07248032fb203925f"},
    {"iid": 56988191, "name": "Địa lí lớp 7C", "id": "6589c5e06d18f6991b0ddc57"},
    {"iid": 56988190, "name": "Lịch sử lớp 7C", "id": "6589c5e0319e4c4bed0b1da3"},
    {"iid": 56988184, "name": "Tiếng anh lớp 7C", "id": "6589c5dfc21f75125004836b"},
    {
        "iid": 56988183,
        "name": "Giáo dục thể chất lớp 7C",
        "id": "6589c5dfb3ffd9c75505a358",
    },
    {
        "iid": 56988186,
        "name": "Giáo dục công dân lớp 7C",
        "id": "6589c5df3eeb63144e02c9ca",
    },
    {
        "iid": 56988185,
        "name": "Hoạt động trải nghiệm lớp 7C",
        "id": "6589c5df0ccf42b3f40b64ca",
    },
    {"iid": 56988182, "name": "Mĩ thuật lớp 7C", "id": "6589c5deef4c6d041b0bc643"},
    {"iid": 56988181, "name": "Âm nhạc lớp 7C", "id": "6589c5d9ce272a617f0405bc"},
    {"iid": 56988178, "name": "Địa lí lớp 7A", "id": "6589c5d95d2ea90e3a0bebd9"},
    {"iid": 56988180, "name": "Ngữ văn lớp 7C", "id": "6589c5d941215159ab0ef6ce"},
    {"iid": 56988179, "name": "Toán lớp 7C", "id": "6589c5d90828c42dfe0b9ed0"},
    {"iid": 56988174, "name": "Công nghệ lớp 7A", "id": "6589c5d8acd8c64f94094576"},
    {"iid": 56988177, "name": "Lịch sử lớp 7A", "id": "6589c5d86fa8b1534d0d9e01"},
    {"iid": 56988175, "name": "Vật lí lớp 7A", "id": "6589c5d82d29a97aef0aa56b"},
    {"iid": 56988176, "name": "Sinh học lớp 7A", "id": "6589c5d825b75c05240cdaed"},
    {"iid": 56988171, "name": "Tiếng anh lớp 7A", "id": "6589c5d767020aef490ce2ca"},
    {
        "iid": 56988173,
        "name": "Giáo dục công dân lớp 7A",
        "id": "6589c5d74f7fddf1ad0751fb",
    },
    {
        "iid": 56988170,
        "name": "Giáo dục thể chất lớp 7A",
        "id": "6589c5d73c5b31bf5b0e3b79",
    },
    {
        "iid": 56988172,
        "name": "Hoạt động trải nghiệm lớp 7A",
        "id": "6589c5d7031e5494f109e4d4",
    },
    {"iid": 56988166, "name": "Toán lớp 7A", "id": "6589c5d6ec8ef6676b0ec163"},
    {"iid": 56988168, "name": "Âm nhạc lớp 7A", "id": "6589c5d69cb16095be066b7c"},
    {"iid": 56988169, "name": "Mĩ thuật lớp 7A", "id": "6589c5d640f5254c5d0e12b8"},
    {"iid": 56988167, "name": "Ngữ văn lớp 7A", "id": "6589c5d62b7932e29c0c08bc"},
    {"iid": 56988162, "name": "Vật lí lớp 6A", "id": "6589c5d580a091b0ee00ca19"},
    {"iid": 56988165, "name": "Địa lí lớp 6A", "id": "6589c5d55763db004e0099e5"},
    {"iid": 56988164, "name": "Lịch sử lớp 6A", "id": "6589c5d556c02b2ab6000fec"},
    {"iid": 56988163, "name": "Sinh học lớp 6A", "id": "6589c5d530643ff88e0afbba"},
    {"iid": 56988161, "name": "Công nghệ lớp 6A", "id": "6589c5d4efb93457b209188d"},
    {
        "iid": 56988159,
        "name": "Hoạt động trải nghiệm lớp 6A",
        "id": "6589c5d4ddfaa4961e0b2ce6",
    },
    {
        "iid": 56988157,
        "name": "Giáo dục thể chất lớp 6A",
        "id": "6589c5d4cc26d9e3a7057fe6",
    },
    {"iid": 56988158, "name": "Tiếng anh lớp 6A", "id": "6589c5d49e8342256d00559c"},
    {
        "iid": 56988160,
        "name": "Giáo dục công dân lớp 6A",
        "id": "6589c5d43e56cfd29300fda8",
    },
    {"iid": 56988156, "name": "Mĩ thuật lớp 6A", "id": "6589c5d3fb52d91dbd05efa5"},
    {"iid": 56988154, "name": "Ngữ văn lớp 6A", "id": "6589c5d3507093362801ef64"},
    {"iid": 56988153, "name": "Toán lớp 6A", "id": "6589c5d34ec3ba27d30a9312"},
    {"iid": 56988155, "name": "Âm nhạc lớp 6A", "id": "6589c5d300b7eeaf92093297"},
    {"iid": 56988149, "name": "Vật lí lớp 6C", "id": "6589c5d2f37ab610c90b9a2c"},
    {"iid": 56988148, "name": "Công nghệ lớp 6C", "id": "6589c5d2a03a2dc27e0913f8"},
    {"iid": 56988150, "name": "Sinh học lớp 6C", "id": "6589c5d28c4c171e220cadf3"},
    {"iid": 56988151, "name": "Lịch sử lớp 6C", "id": "6589c5d250c0d376c4021fa5"},
    {"iid": 56988152, "name": "Địa lí lớp 6C", "id": "6589c5d23fc14fc07a08f824"},
    {
        "iid": 56988147,
        "name": "Giáo dục công dân lớp 6C",
        "id": "6589c5d1e784756f2302c8d7",
    },
    {
        "iid": 56988144,
        "name": "Giáo dục thể chất lớp 6C",
        "id": "6589c5d1bc960ea9e30f7519",
    },
    {"iid": 56988145, "name": "Tiếng anh lớp 6C", "id": "6589c5d18c159ec138031d12"},
    {"iid": 56988143, "name": "Mĩ thuật lớp 6C", "id": "6589c5d162cf143a75010382"},
    {
        "iid": 56988146,
        "name": "Hoạt động trải nghiệm lớp 6C",
        "id": "6589c5d10bb12a522a07e787",
    },
    {"iid": 56988141, "name": "Ngữ văn lớp 6C", "id": "6589c5d0b3c2569b2907abd7"},
    {"iid": 56988139, "name": "Địa lí lớp 6B", "id": "6589c5d0717b53effc0bff22"},
    {"iid": 56988142, "name": "Âm nhạc lớp 6C", "id": "6589c5d04705fbaae409aee1"},
    {"iid": 56988138, "name": "Lịch sử lớp 6B", "id": "6589c5d0291543401600e884"},
    {"iid": 56988140, "name": "Toán lớp 6C", "id": "6589c5d00416f51b7b06ef8f"},
    {"iid": 56988135, "name": "Công nghệ lớp 6B", "id": "6589c5cfdb4c7de4a709a9b4"},
    {"iid": 56988136, "name": "Vật lí lớp 6B", "id": "6589c5cf8bec5fe9f60c9b87"},
    {"iid": 56988137, "name": "Sinh học lớp 6B", "id": "6589c5cf6661832ff10fb152"},
    {
        "iid": 56988133,
        "name": "Hoạt động trải nghiệm lớp 6B",
        "id": "6589c5cefd383f88ac0fd153",
    },
    {
        "iid": 56988134,
        "name": "Giáo dục công dân lớp 6B",
        "id": "6589c5cedccc4046020b991f",
    },
    {"iid": 56988132, "name": "Tiếng anh lớp 6B", "id": "6589c5cec5c0a84dc30131be"},
    {
        "iid": 56988131,
        "name": "Giáo dục thể chất lớp 6B",
        "id": "6589c5ce1808d63c780a1da0",
    },
    {"iid": 56988130, "name": "Mĩ thuật lớp 6B", "id": "6589c5cd9da7ffc7de0f2fb4"},
    {"iid": 56988129, "name": "Âm nhạc lớp 6B", "id": "6589c5cd19dfbff4750b56a6"},
    {"iid": 56988128, "name": "Ngữ văn lớp 6B", "id": "6589c5cccbf250edbc0dbd45"},
    {"iid": 56988126, "name": "Địa lí lớp 8B", "id": "6589c5cc7e3c043c5b0868ec"},
    {"iid": 56988125, "name": "Lịch sử lớp 8B", "id": "6589c5cc65ca5997950c329e"},
    {"iid": 56988127, "name": "Toán lớp 6B", "id": "6589c5cc16c0422ee5023b2e"},
    {"iid": 56988123, "name": "Hoá học lớp 8B", "id": "6589c5cbcfdf4c82b10e3b8d"},
    {"iid": 56988121, "name": "Công nghệ lớp 8B", "id": "6589c5cbcccf06ae1a0aca22"},
    {"iid": 56988122, "name": "Vật lí lớp 8B", "id": "6589c5cbaf94d129bc06151a"},
    {"iid": 56988124, "name": "Sinh học lớp 8B", "id": "6589c5cb19633214a00ddeae"},
    {
        "iid": 56988117,
        "name": "Giáo dục thể chất lớp 8B",
        "id": "6589c5cad8af5ca8260980c7",
    },
    {"iid": 56988118, "name": "Tiếng anh lớp 8B", "id": "6589c5ca9cb5cf53980c1aa5"},
    {
        "iid": 56988120,
        "name": "Giáo dục công dân lớp 8B",
        "id": "6589c5ca39cd6c34f80b7e04",
    },
    {
        "iid": 56988119,
        "name": "Hoạt động trải nghiệm lớp 8B",
        "id": "6589c5ca1b0d6ddc630f0804",
    },
    {"iid": 56988114, "name": "Ngữ văn lớp 8B", "id": "6589c5c981df226cc10eb695"},
    {"iid": 56988115, "name": "Âm nhạc lớp 8B", "id": "6589c5c961297d89920e83d9"},
    {"iid": 56988116, "name": "Mĩ thuật lớp 8B", "id": "6589c5c95095b9cf010dd58c"},
    {"iid": 56988113, "name": "Toán lớp 8B", "id": "6589c5c8867b4ce527072c1e"},
    {"iid": 56988111, "name": "Lịch sử lớp 8A", "id": "6589c5c86d0577e8170a4ed1"},
    {"iid": 56988112, "name": "Địa lí lớp 8A", "id": "6589c5c862c08466b304d7e0"},
    {"iid": 56988108, "name": "Vật lí lớp 8A", "id": "6589c5c74a7b2ffa39028d2d"},
    {"iid": 56988110, "name": "Sinh học lớp 8A", "id": "6589c5c72415ce838102e238"},
    {"iid": 56988109, "name": "Hoá học lớp 8A", "id": "6589c5c70c1a0b54ce030b5a"},
    {"iid": 56988107, "name": "Công nghệ lớp 8A", "id": "6589c5c6c5278d44c00c8452"},
    {"iid": 56988104, "name": "Tiếng anh lớp 8A", "id": "6589c5c6ba2d672bc60698b8"},
    {
        "iid": 56988106,
        "name": "Giáo dục công dân lớp 8A",
        "id": "6589c5c64adabc4c000761c2",
    },
    {
        "iid": 56988105,
        "name": "Hoạt động trải nghiệm lớp 8A",
        "id": "6589c5c64210acd7b90f3657",
    },
    {"iid": 56988102, "name": "Mĩ thuật lớp 8A", "id": "6589c5c5f3561b894700385a"},
    {
        "iid": 56988103,
        "name": "Giáo dục thể chất lớp 8A",
        "id": "6589c5c5cd8500cf1e03161e",
    },
    {"iid": 56988101, "name": "Âm nhạc lớp 8A", "id": "6589c5c5b4f7cd02e40cd40c"},
    {"iid": 56988098, "name": "Địa lí lớp 8C", "id": "6589c5c432b7d19b990b7206"},
    {"iid": 56988097, "name": "Lịch sử lớp 8C", "id": "6589c5c41adead3cad0fe2f9"},
    {"iid": 56988100, "name": "Ngữ văn lớp 8A", "id": "6589c5c413fe629005058510"},
    {"iid": 56988099, "name": "Toán lớp 8A", "id": "6589c5c4129b054fba013425"},
    {"iid": 56988096, "name": "Sinh học lớp 8C", "id": "6589c5c3c9a599a1b20061c5"},
    {"iid": 56988095, "name": "Hoá học lớp 8C", "id": "6589c5c394ef9b71930b9aba"},
    {
        "iid": 56988092,
        "name": "Giáo dục công dân lớp 8C",
        "id": "6589c5c33410e4085d04fa9f",
    },
    {"iid": 56988093, "name": "Công nghệ lớp 8C", "id": "6589c5c325c56a7861063be7"},
    {"iid": 56988094, "name": "Vật lí lớp 8C", "id": "6589c5c31b4443a43404a57d"},
    {"iid": 56988087, "name": "Âm nhạc lớp 8C", "id": "6589c5c2f5c14222ec0a78e9"},
    {
        "iid": 56988089,
        "name": "Giáo dục thể chất lớp 8C",
        "id": "6589c5c2b3f80c63d2071c4c",
    },
    {"iid": 56988088, "name": "Mĩ thuật lớp 8C", "id": "6589c5c27248032fb203925c"},
    {
        "iid": 56988091,
        "name": "Hoạt động trải nghiệm lớp 8C",
        "id": "6589c5c26d18f6991b0ddc54",
    },
    {"iid": 56988090, "name": "Tiếng anh lớp 8C", "id": "6589c5c2319e4c4bed0b1da0"},
    {"iid": 56988082, "name": "Sinh học lớp 9B", "id": "6589c5c1ef4c6d041b0bc640"},
    {"iid": 56988084, "name": "Địa lí lớp 9B", "id": "6589c5c1c21f751250048368"},
    {"iid": 56988083, "name": "Lịch sử lớp 9B", "id": "6589c5c1b3ffd9c75505a355"},
    {"iid": 56988086, "name": "Ngữ văn lớp 8C", "id": "6589c5c13eeb63144e02c9c7"},
    {"iid": 56988085, "name": "Toán lớp 8C", "id": "6589c5c10ccf42b3f40b64c7"},
    {"iid": 56988081, "name": "Hoá học lớp 9B", "id": "6589c5c0ce272a617f0405b9"},
    {
        "iid": 56988077,
        "name": "Hoạt động trải nghiệm lớp 9B",
        "id": "6589c5c06fa8b1534d0d9dfe",
    },
    {
        "iid": 56988078,
        "name": "Giáo dục công dân lớp 9B",
        "id": "6589c5c05d2ea90e3a0bebd6",
    },
    {"iid": 56988080, "name": "Vật lí lớp 9B", "id": "6589c5c041215159ab0ef6cb"},
    {"iid": 56988079, "name": "Công nghệ lớp 9B", "id": "6589c5c00828c42dfe0b9ecd"},
    {"iid": 56988074, "name": "Mĩ thuật lớp 9B", "id": "6589c5bfacd8c64f94094573"},
    {"iid": 56988073, "name": "Âm nhạc lớp 9B", "id": "6589c5bf4f7fddf1ad0751f8"},
    {
        "iid": 56988075,
        "name": "Giáo dục thể chất lớp 9B",
        "id": "6589c5bf2d29a97aef0aa568",
    },
    {"iid": 56988076, "name": "Tiếng anh lớp 9B", "id": "6589c5bf25b75c05240cdaea"},
    {"iid": 56988072, "name": "Ngữ văn lớp 9B", "id": "6589c5bf031e5494f109e4d1"},
    {"iid": 56988068, "name": "Sinh học lớp 9A", "id": "6589c5be9cb16095be066b79"},
    {"iid": 56988071, "name": "Toán lớp 9B", "id": "6589c5be67020aef490ce2c7"},
    {"iid": 56988069, "name": "Lịch sử lớp 9A", "id": "6589c5be40f5254c5d0e12b5"},
    {"iid": 56988070, "name": "Địa lí lớp 9A", "id": "6589c5be3c5b31bf5b0e3b76"},
    {"iid": 56988067, "name": "Hoá học lớp 9A", "id": "6589c5be2b7932e29c0c08b9"},
    {"iid": 56988066, "name": "Vật lí lớp 9A", "id": "6589c5bdec8ef6676b0ec160"},
    {"iid": 56988062, "name": "Tiếng anh lớp 9A", "id": "6589c5bd80a091b0ee00ca16"},
    {"iid": 56988065, "name": "Công nghệ lớp 9A", "id": "6589c5bd5763db004e0099e2"},
    {
        "iid": 56988064,
        "name": "Giáo dục công dân lớp 9A",
        "id": "6589c5bd56c02b2ab6000fe9",
    },
    {
        "iid": 56988063,
        "name": "Hoạt động trải nghiệm lớp 9A",
        "id": "6589c5bd30643ff88e0afbb7",
    },
    {
        "iid": 56988061,
        "name": "Giáo dục thể chất lớp 9A",
        "id": "6589c5bcefb93457b209188a",
    },
    {"iid": 56988059, "name": "Âm nhạc lớp 9A", "id": "6589c5bcddfaa4961e0b2ce3"},
    {"iid": 56988057, "name": "Toán lớp 9A", "id": "6589c5bccc26d9e3a7057fe3"},
    {"iid": 56988058, "name": "Ngữ văn lớp 9A", "id": "6589c5bc9e8342256d005599"},
    {"iid": 56988060, "name": "Mĩ thuật lớp 9A", "id": "6589c5bc3e56cfd29300fda5"},
    {"iid": 56988056, "name": "Địa lí lớp 9C", "id": "6589c5bbfb52d91dbd05efa2"},
    {"iid": 56988054, "name": "Sinh học lớp 9C", "id": "6589c5bb507093362801ef61"},
    {"iid": 56988053, "name": "Hoá học lớp 9C", "id": "6589c5bb4ec3ba27d30a930f"},
    {"iid": 56988052, "name": "Vật lí lớp 9C", "id": "6589c5bb3fc14fc07a08f821"},
    {"iid": 56988055, "name": "Lịch sử lớp 9C", "id": "6589c5bb00b7eeaf92093294"},
    {
        "iid": 56988049,
        "name": "Hoạt động trải nghiệm lớp 9C",
        "id": "6589c5baf37ab610c90b9a29",
    },
    {
        "iid": 56988047,
        "name": "Giáo dục thể chất lớp 9C",
        "id": "6589c5bae784756f2302c8d4",
    },
    {"iid": 56988048, "name": "Tiếng anh lớp 9C", "id": "6589c5baa03a2dc27e0913f5"},
    {
        "iid": 56988050,
        "name": "Giáo dục công dân lớp 9C",
        "id": "6589c5ba8c4c171e220cadf0",
    },
    {"iid": 56988051, "name": "Công nghệ lớp 9C", "id": "6589c5ba50c0d376c4021fa2"},
    {"iid": 56988044, "name": "Ngữ văn lớp 9C", "id": "6589c5b9bc960ea9e30f7516"},
    {"iid": 56988045, "name": "Âm nhạc lớp 9C", "id": "6589c5b98c159ec138031d0f"},
    {"iid": 56988043, "name": "Toán lớp 9C", "id": "6589c5b962cf143a7501037f"},
    {"iid": 56988046, "name": "Mĩ thuật lớp 9C", "id": "6589c5b90bb12a522a07e784"},
]
school = lms.New(dmn="ve", type_dmn="bgg")

for c in list_course:
    add_role_to_course(school, iid_course=c["iid"], iid_role=56988217)
