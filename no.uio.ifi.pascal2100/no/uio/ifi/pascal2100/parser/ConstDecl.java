package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.scanner.*;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;


import no.uio.ifi.pascal2100.main.*;


/**
 * <h1>v</h1>
 *
 * <p>Parse a Pascal ConstDecl  as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class ConstDecl extends PascalDecl {
/* name ---=--- constant--;*/
	Constant c;
	String name;
	public ConstDecl nextconstdec;
	public ConstDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}

	
	 /**
     * Parse a ConstDecl.
     * @param Scanner Tokens.
     * @return the ConstDecl object of the parse tree.
     */
	public static ConstDecl parse(Scanner s) {
		
		enterParser("const decl");
		s.test(nameToken);
		ConstDecl cd = new ConstDecl(s.curToken.id, s.curLineNum());
		cd.name=s.curToken.id;
		s.readNextToken();
		
		s.skip(equalToken);
		
		
		cd.c=Constant.parse(s);
		/*s.readNextToken();*/
		
		s.skip(semicolonToken);
		leaveParser("const decl");
		return cd;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<const decl> " + name + " on line " + lineNum;
	}

	@Override void prettyPrint() {
		
		Main.log.prettyPrint(name);
		Main.log.prettyPrint(" = ");
		if (c!=null)c.prettyPrint();
		 Main.log.prettyPrint(" ; ");
		 Main.log.prettyIndent();
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		/*curScope.addDecl(name, this);*/
		if (c!=null){
			c.check(curScope, lib);
			
		}
		
	}
		
}
