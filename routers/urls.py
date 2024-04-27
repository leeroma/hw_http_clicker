from controllers.pages_controller import PagesController
from routers.router import Router

router = Router()
router.get('/', PagesController, 'home')
router.get('/one', PagesController, 'one')
router.get('/two', PagesController, 'two')
router.get('/three', PagesController, 'three')
router.get('/game', PagesController, 'game')
router.post('/add_click', PagesController, 'add_click')
router.post('/refresh', PagesController, 'refresh')
