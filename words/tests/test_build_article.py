import json 
from django.test import TestCase, Client
from ..models import Word, Article, ArticleWord, ArticleManager


client = Client()

class ApiRoutesTest(TestCase):
  def setUp(self):
    self.body = "The guinea pig or domestic guinea pig (Cavia porcellus), also known as cavy or domestic cavy (/ˈkeɪvi/), is a species of rodent belonging to the family Caviidae and the genus Cavia. Despite their common name, guinea pigs are not native to Guinea, nor are they closely biologically related to pigs, and the origin of the name is still unclear. They originated in the Andes of South America. Studies based on biochemistry and hybridization suggest they are domesticated descendants of a closely related species of cavy, such as C. tschudii, and do not exist naturally in the wild.[1][2] They were originally domesticated as livestock, for a source of meat, and continue to be consumed as food. In Western society, the domestic guinea pig has enjoyed widespread popularity as a pocket pet, since its introduction to Europe and North America by European traders in the 16th century. Their docile nature, friendly responsiveness to handling and feeding, and the relative ease of caring for them have made guinea pigs a continuing popular choice of household pet. Organizations devoted to the competitive breeding of guinea pigs have been formed worldwide. Many specialized breeds, with varying coat colors and textures, are selected by breeders. The domestic guinea pig plays an important role in folk culture for many indigenous Andean peoples, especially as a food source. It is also used in folk medicine and in community religious ceremonies.[3] The animals are used for meat and are a culinary staple in the Andes Mountains, where they are known as cuy. In the 1960s a modern breeding program was started in Peru that resulted in large breeds known as cuy mejorados (improved cuy). Marketers tried to increase consumption of the animal outside South America.[4] Biological experimentation on domestic guinea pigs has been carried out since the 17th century. The animals were used so frequently as model organisms in the 19th and 20th centuries that the epithet guinea pig came into use to describe a human test subject. Since that time, they have been largely replaced by other rodents, such as mice and rats. However, they are still used in research, primarily as models to study such human medical conditions as juvenile diabetes, tuberculosis, scurvy (like humans, they require dietary intake of vitamin C), and pregnancy complications."
    self.title = "Guinea Pig"

    self.word1 = Word.objects.create(word='word1', length=5)
    self.word2 = Word.objects.create(word='word22', length=6)
    self.word3 = Word.objects.create(word='word333', length=7)


  def test_get_word_index(self):
    res = client.get('/words/')
    self.assertEqual(res)

    import pdb; pdb.set_trace()