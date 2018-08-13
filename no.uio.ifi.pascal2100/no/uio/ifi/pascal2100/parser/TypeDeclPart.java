package no.uio.ifi.pascal2100.parser;
import no.uio.ifi.pascal2100.scanner.*;
import no.uio.ifi.pascal2100.main.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;

/*type -- typedecl*/

import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>TypeDeclPart</h1>
 *
 * <p>Parse a Pascal TypeDeclPart as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class TypeDeclPart extends PascalSyntax {
 
	public  ArrayList<TypeDecl>  typer= new ArrayList<TypeDecl>();
	Block b;
	TypeDecl td;
	String name;
	public TypeDecl firsttypedecl;
	
	
	public TypeDeclPart(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	
	 /**
     * Parse a TypeDeclPart
     * @param Scanner Tokens.
     * @return the TypeDeclPart object of the parse tree.
     * type ----type decl
     */
	public static TypeDeclPart parse(Scanner s) {
		
		enterParser("type decl part");
		TypeDeclPart tdp = new TypeDeclPart(s.curLineNum());
		s.skip(typeToken);
		
		tdp.firsttypedecl=TypeDecl.parse(s);
		
		tdp.typer.add(tdp.firsttypedecl);
		TypeDecl temptyp= tdp.firsttypedecl;
		
		while(s.curToken.kind==nameToken){
			temptyp.nexttypedec=temptyp=TypeDecl.parse(s);
			
			tdp.typer.add(temptyp);
		}
		leaveParser("type decl part");
		return tdp;
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<type decl part> " + " on line " + lineNum;
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		Main.log.prettyPrint("type");
		TypeDecl localtype= firsttypedecl;
		while (localtype!=null){
			localtype.prettyPrint();
		
			localtype=localtype.nexttypedec;
		
		
		}
		
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		TypeDecl localtype= firsttypedecl;
		while (localtype!=null){
			localtype.check(curScope,lib);
			
			localtype=localtype.nexttypedec;
		
		
		}
		
	}

}
