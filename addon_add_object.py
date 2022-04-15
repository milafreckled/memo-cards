bl_info = {
    "name": "Mila's Add-on",
    "author": "Liudmyla Malomuzh",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Tool",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy

"""Klasa materialu"""
class ShaderDiamondOperator(bpy.types.Operator):
    bl_label = "Diamond Operator"
    bl_idname = "shader.diamond_operator" #definicja typu biblioteki materialu, w danym przypadku `SHADER`
    bl_options = {'REGISTER','UNDO'}
        
        
    def execute(self, context):
      
        material_diamond = bpy.data.materials.new(name="Diamond") #tworzenie nowego materialu
        material_diamond.use_nodes = True #włączenie węzłow
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get("Principled BSDF"))
        print(material_diamond.node_tree.outputs)
        print(material_diamond.node_tree.inputs)
        material_diamond.node_tree.bl_icon = "NODETREE"
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        material_output.location = (-400, 0)
        """Wezły ze szklanym shaderem, mieszającym załamanie i odbicie pod różnymi kątami"""
        #dodanie wesłu szkła
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #rozmieszczenie węzłu
        glass1_node.location = (-600, 0)
        #ustawienia domyslnego koloru
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        #ustawienie domylnej wartoci IOR (index of refraction)
        glass1_node.inputs[2].default_value = 1.446
        
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass2_node.location = (-600, -150)
        #ustawienia domyslnego koloru
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        #ustawienie domyslnej wartoci IOR
        glass2_node.inputs[2].default_value = 1.450
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.location = (-600, -300)
        #ustawienia domylnego koloru
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        #ustawienie domylnej wartoci IOR
        glass3_node.inputs[2].default_value = 1.450
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.location = (-600, -300)
        #ustawienia domyslnego koloru
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        #ustawienie domyslnej wartoci IOR
        glass3_node.inputs[2].default_value = 1.450
        
        """Węzły, służące do połączenia dwoch shaderow"""
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-400, -50)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False
       
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add2_node.location = (-100, 0)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False
        
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass4_node.location = (-150, -150)
        #ustawienia domylnego koloru
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        #ustawienie domylnej wartoci IOR
        glass4_node.inputs[2].default_value = 1.450
        glass4_node.select = False
        
        """Węzeł, służący do miksowania dwoch shaderow"""
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        mix1_node.location = (200, 0)
        mix1_node.select = False
       
       #połączenie wezłow (nodow) dla uzyskania finalnego wyglądu powierzhni.
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass4_node.outputs[0], add2_node.inputs[1])
        
        material_diamond.node_tree.links.new(add1_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[2])
        
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
    
"""Klasa panelu"""
class MilasPanel(bpy.types.Panel):
    bl_label = "Mila's Add-on" #nagłowek panelu
    bl_idname = "MilasPanel" #id panelu
    bl_space_type = 'VIEW_3D' #typ przestreni
    bl_region_type = 'UI' #miejsce odwzorowania
    bl_category = "Shader Library" #kategoria

    """Funkcja do graficznego odtwarzania panelu"""
    def draw(self, context):
        
        layout = self.layout #zmienna do oznaczenia potocznego układu
        obj = context.object #zmienna do oznaczenia potocznego obiektu
        
       
        row = layout.row() #dodanie nowego wiersza do okna panelu
        row.label(text=f"Active object - {obj.name} ", translate = True) #label z imiem aktywnego obiektu
        row = layout.row() 
        row.label(text=f"Active material - {obj.active_material}") #label z imiem aktywnego materialu
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'CUBE') #operator dodania prymitywu - szescianu
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE') #operator dodania prymitywu - kuli
        row = layout.row()
        row.operator("object.select_random", text="Select random object", icon='OBJECT_DATA') #operator przemiennego zaznaczania/odznaczania wszystkich obiektow
        row = layout.row()
        row.operator("object.delete", icon = 'REMOVE', text='Delete object').confirm = False #operator usunięcia obiektu
        sub = row.row() #podział wierszu
        row.operator("object.duplicate_move_linked", icon = 'DUPLICATE', text='Copy and move') #operator kopiowania i poruszania obiektem
       
        row = layout.row()
        row.label(text="Default material") #powrot do pierwotnego materialu
        row = layout.row()
        row.operator('object.material_slot_remove') #operator usuwania slotu z materialem
        #Dodanie własnego operatora do panelu
        row = layout.row()
        row.label(text="Select a Shader to be added")
        row = layout.row()
        row.operator('shader.diamond_operator') #wywołanie własnego operatora
       
        
        #skalowanie obiektu
        row = layout.row()
        row.label(text="Scale the object")
        col = layout.column_flow(columns=3, align = True) #dodanie układu kolumn
        col.prop(context.active_object, "scale_prop_x") #dodanie własciwosci skalowania w osi X
        col.prop(context.active_object, "scale_prop_y") #dodanie własciwosci skalowania w osi y
        col.prop(context.active_object, "scale_prop_z") #dodanie własciwosci skalowania w osi Z
        
"""Funkcja wywoływana przy zmianie stworzonych właciwo
def update_scale(self, context):
    context.active_object.scale[0] = self.scale_prop_x
    context.active_object.scale[1] = self.scale_prop_y
    context.active_object.scale[2] = self.scale_prop_z

def register():
    bpy.utils.register_class(MilasPanel)
    bpy.utils.register_class(ShaderDiamondOperator)
    bpy.types.Object.scale_prop_x = bpy.props.FloatProperty( #własciwosć do skalowania po osi x
        name = "Scale X",
        description="Scaling object in X axis",
        default=1.0,
        update=update_scale
    )
    bpy.types.Object.scale_prop_y = bpy.props.FloatProperty( #własciwosć do skalowania po osi y
        name = "Scale Y",
        description="Scaling object in Y axia",
        default=1.0,
        update=update_scale
    )
    bpy.types.Object.scale_prop_z = bpy.props.FloatProperty( #własciwosć do skalowania po osi z
        name = "Scale Z",
        description="Scaling object in Z axis",
        default=1.0,
        update=update_scale
    )
    bpy.types.UILayout.alignment = 'CENTRAL'
    bpy.types.Panel.direction = 'VERTICAL'
 


def unregister():
    bpy.utils.unregister_class(MilasPanel)
    bpy.utils.unregister_class(ShaderDiamondOperator)
    del bpy.types.Object.my_global_enum
    del bpy.types.Object.scale_prop_x
    del bpy.types.Object.scale_prop_y
    del bpy.types.Object.scale_prop_z


if __name__ == "__main__":
    register()
