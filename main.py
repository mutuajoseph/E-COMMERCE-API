from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# settings import
from settings.config import settings
# api versions
from api.api_v1.api import api_router

app = FastAPI(
    title="ECOMMERCE API",
    description="Endpoints for Ecommerce backend",
    redoc_url="/developer/redoc",
    docs_url="/developer/docs",
    contact={
        "name": "Joseph Wambua Mutua",
        "email": "wambuajoseph756@gmail.com"
    }
)

# setup the middelware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(api_router,
                   prefix=settings.API_V1_STR,
                   responses={
                       200: {'description': 'Ok'},
                       201: {'description': 'Created'},
                       202: {'description': 'Accepted'},
                       400: {"description": "Bad Request"},
                       401: {"description": "Unauthorized"},
                       403: {"description": "Forbidden"},
                       404: {"description": "Not found"},
                       405: {"description": "Method not allowed"},
                       408: {"description": "Request timeout"},
                       409: {"description": "Conflict"},
                       422: {"description": "Unprocessable entity"},
                       500: {"description": "Internal server error"},
                       502: {"description": "Bad Gateway"},
                       503: {"description": "Service Unavailable"},
                       504: {"description": "Gateway Timeout"},
                   },

                   )

# add the pagination syntax here