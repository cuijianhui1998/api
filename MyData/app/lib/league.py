from collections import OrderedDict
from sqlalchemy import or_

from app.models.league_of_legends.hero import Hero
from app.models.league_of_legends.skin import Skin
from app.models.league_of_legends.spell import Spell
from app.error.error_url import NotFoundDataException



def search_hero(key):
    '''
    :param key: 查询的关键字,称号和名称模糊查询
    :return: 英雄的数据
    '''
    result = OrderedDict(total=0,heros=[])
    heros = Hero.query.filter(or_(Hero.title.contains(key),Hero.hero_name.contains(key))).all()
    if heros:
        for hero in heros:
            data = OrderedDict()
            skins = Skin.query.filter(Skin.skin_name.contains(hero.title))
            spell = Spell.query.filter_by(hero_name=hero.hero_name).first()
            data['称号'] = hero.hero_name
            data['名字'] = hero.title
            data['tags'] = hero.tags.split(',')
            data['背景故事'] = hero.lore
            data['使用技巧'] = hero.allytips
            data['对线技巧'] = hero.enemytips
            data['皮肤'] = [{'id':skin.skin_id,'皮肤名称':skin.skin_name,'皮肤图片':skin.skin_image} for skin in skins]
            data['技能介绍'] = {
                '被动':spell.passive_name,
                '被动图片':'http:{}'.format(spell.passive_image),
                'Q技能':spell.Q_name,
                'Q技能图片': 'http:{}'.format(spell.Q_image),
                'W技能': spell.W_name,
                'W技能图片': 'http:{}'.format(spell.W_image),
                'E技能': spell.E_name,
                'E技能图片': 'http:{}'.format(spell.E_image),
                'R技能': spell.R_name,
                'R技能图片': 'http:{}'.format(spell.R_name),
            }
            result['heros'].append(data)
        result['total'] = len(heros)
        return result
    return NotFoundDataException()

